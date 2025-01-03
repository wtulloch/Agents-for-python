from pydantic import BaseModel, Field
from .conversation_members import ConversationMembers
from typing import Optional
from ._type_aliases import NonEmptyString


class ConversationsResult(BaseModel):
    """Conversations result.

    :param continuation_token: Paging token
    :type continuation_token: str
    :param conversations: List of conversations
    :type conversations:
     list[~microsoft.agents.protocols.models.ConversationMembers]
    """

    continuation_token: Optional[NonEmptyString] = Field(
        None, alias="continuationToken"
    )
    conversations: Optional[list[ConversationMembers]] = Field(
        None, alias="conversations"
    )
