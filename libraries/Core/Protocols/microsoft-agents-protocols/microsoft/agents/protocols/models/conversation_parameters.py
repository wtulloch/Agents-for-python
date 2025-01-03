from pydantic import BaseModel, Field
from typing import Optional
from .channel_account import ChannelAccount
from .activity import Activity
from ._type_aliases import NonEmptyString


class ConversationParameters(BaseModel):
    """Parameters for creating a new conversation.

    :param is_group: IsGroup
    :type is_group: bool
    :param bot: The bot address for this conversation
    :type bot: ~microsoft.agents.protocols.models.ChannelAccount
    :param members: Members to add to the conversation
    :type members: list[~microsoft.agents.protocols.models.ChannelAccount]
    :param topic_name: (Optional) Topic of the conversation (if supported by
     the channel)
    :type topic_name: str
    :param activity: (Optional) When creating a new conversation, use this
     activity as the initial message to the conversation
    :type activity: ~microsoft.agents.protocols.models.Activity
    :param channel_data: Channel specific payload for creating the
     conversation
    :type channel_data: object
    :param tenant_id: (Optional) The tenant ID in which the conversation should be created
    :type tenant_id: str
    """

    is_group: Optional[bool] = Field(None, alias="isGroup")
    bot: Optional[ChannelAccount] = Field(None, alias="bot")
    members: Optional[list[ChannelAccount]] = Field(None, alias="members")
    topic_name: Optional[NonEmptyString] = Field(None, alias="topicName")
    activity: Optional[Activity] = Field(None, alias="activity")
    channel_data: Optional[object] = Field(None, alias="channelData")
    tenant_id: Optional[NonEmptyString] = Field(None, alias="tenantID")
