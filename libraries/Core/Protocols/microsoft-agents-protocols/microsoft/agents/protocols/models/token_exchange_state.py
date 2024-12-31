from pydantic import BaseModel, Field
from .conversation_reference import ConversationReference


class TokenExchangeState(BaseModel):
    """TokenExchangeState

    :param connection_name: The connection name that was used.
    :type connection_name: str
    :param conversation: Gets or sets a reference to the conversation.
    :type conversation: ~microsoft.agents.protocols.models.ConversationReference
    :param relates_to: Gets or sets a reference to a related parent conversation for this token exchange.
    :type relates_to: ~microsoft.agents.protocols.models.ConversationReference
    :param bot_ur: The URL of the bot messaging endpoint.
    :type bot_ur: str
    :param ms_app_id: The bot's registered application ID.
    :type ms_app_id: str
    """

    connection_name: str = Field(None, alias="connectionName")
    conversation: ConversationReference = Field(None, alias="conversation")
    relates_to: ConversationReference = Field(None, alias="relatesTo")
    bot_url: str = Field(None, alias="botUrl")
    ms_app_id: str = Field(None, alias="msAppId")
