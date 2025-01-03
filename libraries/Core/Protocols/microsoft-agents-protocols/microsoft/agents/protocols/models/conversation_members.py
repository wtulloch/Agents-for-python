from pydantic import BaseModel, Field
from .channel_account import ChannelAccount
from typing import Optional
from ._type_aliases import NonEmptyString


class ConversationMembers(BaseModel):
    """Conversation and its members.

    :param id: Conversation ID
    :type id: str
    :param members: List of members in this conversation
    :type members: list[~microsoft.agents.protocols.models.ChannelAccount]
    """

    id: Optional[NonEmptyString] = Field(None, alias="id")
    members: Optional[list[ChannelAccount]] = Field(None, alias="members")
