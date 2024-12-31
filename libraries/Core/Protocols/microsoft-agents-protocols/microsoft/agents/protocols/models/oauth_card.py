from pydantic import BaseModel, Field
from .card_action import CardAction


class OAuthCard(BaseModel):
    """A card representing a request to perform a sign in via OAuth.

    :param text: Text for signin request
    :type text: str
    :param connection_name: The name of the registered connection
    :type connection_name: str
    :param buttons: Action to use to perform signin
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    """

    text: str = Field(None, alias="text")
    connection_name: str = Field(None, alias="connectionName")
    buttons: list[CardAction] = Field(None, alias="buttons")
    token_exchange_resource: object = Field(None, alias="tokenExchangeResource")
