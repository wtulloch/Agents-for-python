from pydantic import BaseModel, Field
from .card_action import CardAction


class SuggestedActions(BaseModel):
    """SuggestedActions that can be performed.

    :param to: Ids of the recipients that the actions should be shown to.
     These Ids are relative to the channelId and a subset of all recipients of
     the activity
    :type to: list[str]
    :param actions: Actions that can be shown to the user
    :type actions: list[~microsoft.agents.protocols.models.CardAction]
    """

    to: list[str] = Field(None, alias="to")
    actions: list[CardAction] = Field(None, alias="actions")
