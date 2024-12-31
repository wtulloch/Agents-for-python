from pydantic import BaseModel, Field
from .adaptive_card_invoke_action import AdaptiveCardInvokeAction
from .token_exchange_invoke_request import TokenExchangeInvokeRequest


class AdaptiveCardInvokeValue(BaseModel):
    """AdaptiveCardInvokeResponse.

    Defines the structure that arrives in the Activity.Value for Invoke activity with Name of 'adaptiveCard/action'.

    :param action: The action of this adaptive card invoke action value.
    :type action: :class:`botframework.schema.models.AdaptiveCardInvokeAction`
    :param authentication: The TokenExchangeInvokeRequest for this adaptive card invoke action value.
    :type authentication: :class:`botframework.schema.models.TokenExchangeInvokeRequest`
    :param state: The 'state' or magic code for an OAuth flow.
    :type state: str
    """

    action: AdaptiveCardInvokeAction = Field(None, alias="action")
    authentication: TokenExchangeInvokeRequest = Field(None, alias="authentication")
    state: str = Field(None, alias="state")
