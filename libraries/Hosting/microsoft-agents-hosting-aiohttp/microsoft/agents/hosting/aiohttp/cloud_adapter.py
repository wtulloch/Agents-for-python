# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import Awaitable, Callable, Optional

from aiohttp.web import (
    Request,
    Response,
    json_response,
    WebSocketResponse,
    HTTPBadRequest,
    HTTPMethodNotAllowed,
    HTTPUnauthorized,
    HTTPUnsupportedMediaType,
)
from microsoft.agents.authentication import ClaimsIdentity
from microsoft.agents.core.models import (
    Activity,
    DeliveryModes,
    InvokeResponse,
)
from microsoft.agents.connector import ConnectorClient
from microsoft.agents.botbuilder import (
    Bot,
    ChannelServiceAdapter,
    ChannelServiceClientFactoryBase,
    MessageFactory,
    Middleware,
    TurnContext,
)
from botbuilder.integration.aiohttp.streaming import AiohttpWebSocket
from botframework.connector import AsyncBfPipeline, BotFrameworkConnectorConfiguration
from botframework.connector.auth import (
    AuthenticateRequestResult,
    BotFrameworkAuthentication,
    BotFrameworkAuthenticationFactory,
    ConnectorFactory,
    MicrosoftAppCredentials,
)

from .bot_framework_http_adapter_integration_base import (
    BotFrameworkHttpAdapterIntegrationBase,
)

from .bot_http_adapter import BotHttpAdapter


class CloudAdapter(ChannelServiceAdapter, BotHttpAdapter):
    def __init__(self, channel_service_client_factory: ChannelServiceClientFactoryBase, *middlewares: Middleware):
        """
        Initializes a new instance of the CloudAdapter class.

        :param bot_framework_authentication: Optional BotFrameworkAuthentication instance
        """

        if middlewares:
            for middleware in middlewares:
                self.use(middleware)
        
        async def on_turn_error(context: TurnContext, error: Exception):
            error_message = f"Exception caught : {error}"
            
            await context.send_activity(MessageFactory.text(error_message))
            
            # Send a trace activity
            await context.send_trace_activity("OnTurnError Trace", error_message, "https://www.botframework.com/schemas/error", "TurnError")
        
        self.on_turn_error = on_turn_error

        super().__init__(channel_service_client_factory)

    async def process(self, request: Request, bot: Bot) -> Optional[Response]:
        if not request:
            raise TypeError("CloudAdapter.process: request can't be None")
        if not bot:
            raise TypeError("CloudAdapter.process: bot can't be None")

        if request.method == "POST":
            # Deserialize the incoming Activity
            if "application/json" in request.headers["Content-Type"]:
                body = await request.json()
            else:
                raise HTTPUnsupportedMediaType()

            activity: Activity = Activity.model_validate_json(body)
            # TODO: Add the ability to pass in the ClaimsIdentity
            auth_header = request.headers.get(self._AUTH_HEADER_NAME)
            claims_identity: ClaimsIdentity = request.get("claims_identity")

            # A POST request must contain an Activity
            if not activity.type or not activity.conversation or not activity.conversation.id:
                raise HTTPBadRequest

            try:
                # Process the inbound activity with the bot
                invoke_response = await self.process_activity(
                    claims_identity, activity, bot.on_turn
                )
                if activity.type == "invoke" or activity.delivery_mode == DeliveryModes.expect_replies:
                    # Invoke and ExpectReplies cannot be performed async, the response must be written before the calling thread is released.
                    return json_response(
                        data=invoke_response.body, status=invoke_response.status
                    )
                
                return Response(status=202)
            except PermissionError:
                raise HTTPUnauthorized
        else:
            raise HTTPMethodNotAllowed

    async def _connect(
        self, bot: Bot, request: Request, ws_response: WebSocketResponse
    ):
        if ws_response is None:
            raise TypeError("ws_response can't be None")

        # Grab the auth header from the inbound http request
        auth_header = request.headers.get(self._AUTH_HEADER_NAME)
        # Grab the channelId which should be in the http headers
        channel_id = request.headers.get(self._CHANNEL_ID_HEADER_NAME)

        authentication_request_result = (
            await self.bot_framework_authentication.authenticate_streaming_request(
                auth_header, channel_id
            )
        )

        # Transition the request to a WebSocket connection
        await ws_response.prepare(request)
        bf_web_socket = AiohttpWebSocket(ws_response)

        streaming_activity_processor = _StreamingActivityProcessor(
            authentication_request_result, self, bot, bf_web_socket
        )

        await streaming_activity_processor.listen()


class _StreamingActivityProcessor(StreamingActivityProcessor):
    def __init__(
        self,
        authenticate_request_result: AuthenticateRequestResult,
        adapter: CloudAdapter,
        bot: Bot,
        web_socket: AiohttpWebSocket = None,
    ) -> None:
        self._authenticate_request_result = authenticate_request_result
        self._adapter = adapter

        # Internal reuse of the existing StreamingRequestHandler class
        self._request_handler = StreamingRequestHandler(bot, self, web_socket)

        # Fix up the connector factory so connector create from it will send over this connection
        self._authenticate_request_result.connector_factory = (
            _StreamingConnectorFactory(self._request_handler)
        )

    async def listen(self):
        await self._request_handler.listen()

    async def process_streaming_activity(
        self,
        activity: Activity,
        bot_callback_handler: Callable[[TurnContext], Awaitable],
    ) -> InvokeResponse:
        return await self._adapter.process_activity(
            self._authenticate_request_result, activity, bot_callback_handler
        )


class _StreamingConnectorFactory(ConnectorFactory):
    def __init__(self, request_handler: StreamingRequestHandler) -> None:
        self._request_handler = request_handler
        self._service_url = None

    async def create(
        self, service_url: str, audience: str  # pylint: disable=unused-argument
    ) -> ConnectorClient:
        if not self._service_url:
            self._service_url = service_url
        elif service_url != self._service_url:
            raise RuntimeError(
                "This is a streaming scenario, all connectors from this factory must all be for the same url."
            )

        # TODO: investigate if Driver and pipeline should be moved here
        streaming_driver = StreamingHttpDriver(self._request_handler)
        config = BotFrameworkConnectorConfiguration(
            MicrosoftAppCredentials.empty(),
            service_url,
            pipeline_type=AsyncBfPipeline,
            driver=streaming_driver,
        )
        streaming_driver.config = config
        connector_client = ConnectorClient(None, custom_configuration=config)

        return connector_client
