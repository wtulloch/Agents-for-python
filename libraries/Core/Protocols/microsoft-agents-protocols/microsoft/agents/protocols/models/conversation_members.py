from pydantic import BaseModel, Field
from .channel_account import ChannelAccount


class ConversationMembers(BaseModel):
    """Conversation and its members.

    :param id: Conversation ID
    :type id: str
    :param members: List of members in this conversation
    :type members: list[~microsoft.agents.protocols.models.ChannelAccount]
    """

    id: str = Field(None, alias="id")
    members: list[ChannelAccount] = Field(None, alias="members")
