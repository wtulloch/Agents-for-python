from pydantic import BaseModel, Field
from .conversation_members import ConversationMembers


class ConversationsResult(BaseModel):
    """Conversations result.

    :param continuation_token: Paging token
    :type continuation_token: str
    :param conversations: List of conversations
    :type conversations:
     list[~microsoft.agents.protocols.models.ConversationMembers]
    """

    continuation_token: str = Field(None, alias="continuationToken")
    conversations: list[ConversationMembers] = Field(None, alias="conversations")
