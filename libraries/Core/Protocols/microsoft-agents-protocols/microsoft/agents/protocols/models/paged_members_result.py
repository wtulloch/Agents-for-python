from pydantic import BaseModel, Field
from .channel_account import ChannelAccount
from ._type_aliases import NonEmptyString
from typing import Optional


class PagedMembersResult(BaseModel):
    """Page of members.

    :param continuation_token: Paging token
    :type continuation_token: str
    :param members: The Channel Accounts.
    :type members: list[~microsoft.agents.protocols.models.ChannelAccount]
    """

    continuation_token: Optional[NonEmptyString] = Field(
        None, alias="continuationToken"
    )
    members: Optional[list[ChannelAccount]] = Field(None, alias="members")
