from pydantic import BaseModel, Field
from typing import Optional
from .card_action import CardAction
from ._type_aliases import NonEmptyString


class SuggestedActions(BaseModel):
    """SuggestedActions that can be performed.

    :param to: Ids of the recipients that the actions should be shown to.
     These Ids are relative to the channelId and a subset of all recipients of
     the activity
    :type to: list[str]
    :param actions: Actions that can be shown to the user
    :type actions: list[~microsoft.agents.protocols.models.CardAction]
    """

    to: Optional[list[NonEmptyString]] = Field(None, alias="to")
    actions: Optional[list[CardAction]] = Field(None, alias="actions")
