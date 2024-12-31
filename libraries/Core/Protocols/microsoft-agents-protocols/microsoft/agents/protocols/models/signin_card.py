from pydantic import BaseModel, Field
from .card_action import CardAction


class SigninCard(BaseModel):
    """A card representing a request to sign in.

    :param text: Text for signin request
    :type text: str
    :param buttons: Action to use to perform signin
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    """

    text: str = Field(None, alias="text")
    buttons: list[CardAction] = Field(None, alias="buttons")
