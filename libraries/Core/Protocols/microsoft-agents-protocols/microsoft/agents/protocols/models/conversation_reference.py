from pydantic import BaseModel, Field
from .channel_account import ChannelAccount
from .conversation_account import ConversationAccount


class ConversationReference(BaseModel):
    """An object relating to a particular point in a conversation.

    :param activity_id: (Optional) ID of the activity to refer to
    :type activity_id: str
    :param user: (Optional) User participating in this conversation
    :type user: ~microsoft.agents.protocols.models.ChannelAccount
    :param bot: Bot participating in this conversation
    :type bot: ~microsoft.agents.protocols.models.ChannelAccount
    :param conversation: Conversation reference
    :type conversation: ~microsoft.agents.protocols.models.ConversationAccount
    :param channel_id: Channel ID
    :type channel_id: str
    :param locale: A locale name for the contents of the text field.
        The locale name is a combination of an ISO 639 two- or three-letter
        culture code associated with a language and an ISO 3166 two-letter
        subculture code associated with a country or region.
        The locale name can also correspond to a valid BCP-47 language tag.
    :type locale: str
    :param service_url: Service endpoint where operations concerning the
     referenced conversation may be performed
    :type service_url: str
    """

    activity_id: str = Field(None, alias="activityId")
    user: ChannelAccount = Field(None, alias="user")
    bot: ChannelAccount = Field(None, alias="bot")
    conversation: ConversationAccount = Field(None, alias="conversation")
    channel_id: str = Field(None, alias="channelId")
    locale: str = Field(None, alias="locale")
    service_url: str = Field(None, alias="serviceUrl")
