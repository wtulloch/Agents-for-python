from pydantic import BaseModel, Field
from typing import Optional
from .card_action import CardAction
from ._type_aliases import NonEmptyString


class SigninCard(BaseModel):
    """A card representing a request to sign in.

    :param text: Text for signin request
    :type text: str
    :param buttons: Action to use to perform signin
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    """

    text: Optional[NonEmptyString] = Field(None, alias="text")
    buttons: Optional[list[CardAction]] = Field(None, alias="buttons")
