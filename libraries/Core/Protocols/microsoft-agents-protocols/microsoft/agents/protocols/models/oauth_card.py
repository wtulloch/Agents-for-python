from pydantic import BaseModel, Field
from typing import Optional
from .card_action import CardAction
from ._type_aliases import NonEmptyString


class OAuthCard(BaseModel):
    """A card representing a request to perform a sign in via OAuth.

    :param text: Text for signin request
    :type text: str
    :param connection_name: The name of the registered connection
    :type connection_name: str
    :param buttons: Action to use to perform signin
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    """

    text: Optional[NonEmptyString] = Field(None, alias="text")
    connection_name: Optional[NonEmptyString] = Field(None, alias="connectionName")
    buttons: Optional[list[CardAction]] = Field(None, alias="buttons")
    token_exchange_resource: Optional[object] = Field(
        None, alias="tokenExchangeResource"
    )
