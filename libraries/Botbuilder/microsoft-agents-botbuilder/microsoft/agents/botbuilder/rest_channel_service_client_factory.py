from typing import Any, Optional

from microsoft.agents.authentication import (
    AuthenticationConstants,
    ClaimsIdentity,
    Connections,
)
from microsoft.agents.connector import ConnectorClientBase

from .channel_service_client_factory_base import ChannelServiceClientFactoryBase


class RestChannelServiceClientFactory(ChannelServiceClientFactoryBase):
    def __init__(
        self,
        configuration: Any,
        connections: Connections,
        token_service_endpoint=AuthenticationConstants.BOT_FRAMEWORK_OAUTH_URL,
        token_service_audience=AuthenticationConstants.BOT_FRAMEWORK_SCOPE,
        **kwargs: Any
    ) -> None:
        self._connections = connections
        self._token_service_endpoint = token_service_endpoint
        self._token_service_audience = token_service_audience

    async def create_connector_client(
        self,
        claims_identity: ClaimsIdentity,
        service_url: str,
        audience: str,
        scopes: Optional[list[str]] = None,
        use_anonymous: bool = False,
    ) -> ConnectorClientBase:
        pass
