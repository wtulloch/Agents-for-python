from pydantic import BaseModel, Field
from .channel_account import ChannelAccount
from .activity import Activity


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

    is_group: bool = Field(None, alias="isGroup")
    bot: ChannelAccount = Field(None, alias="bot")
    members: list[ChannelAccount] = Field(None, alias="members")
    topic_name: str = Field(None, alias="topicName")
    activity: Activity = Field(None, alias="activity")
    channel_data: object = Field(None, alias="channelData")
    tenant_id: str = Field(None, alias="tenantID")
