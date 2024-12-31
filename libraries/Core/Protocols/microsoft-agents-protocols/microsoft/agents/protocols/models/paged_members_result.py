from pydantic import BaseModel, Field
from .channel_account import ChannelAccount


class PagedMembersResult(BaseModel):
    """Page of members.

    :param continuation_token: Paging token
    :type continuation_token: str
    :param members: The Channel Accounts.
    :type members: list[~microsoft.agents.protocols.models.ChannelAccount]
    """

    continuation_token: str = Field(None, alias="continuationToken")
    members: list[ChannelAccount] = Field(None, alias="members")
