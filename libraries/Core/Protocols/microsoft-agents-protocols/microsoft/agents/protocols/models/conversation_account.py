from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class ConversationAccount(BaseModel):
    """Conversation account represents the identity of the conversation within a channel.

    :param is_group: Indicates whether the conversation contains more than two
     participants at the time the activity was generated
    :type is_group: bool
    :param conversation_type: Indicates the type of the conversation in
     channels that distinguish between conversation types
    :type conversation_type: str
    :param id: Channel id for the user or bot on this channel (Example:
     joe@smith.com, or @joesmith or 123456)
    :type id: str
    :param name: Display friendly name
    :type name: str
    :param aad_object_id: This account's object ID within Azure Active
     Directory (AAD)
    :type aad_object_id: str
    :param role: Role of the entity behind the account (Example: User, Bot, Skill
     etc.). Possible values include: 'user', 'bot', 'skill'
    :type role: str or ~microsoft.agents.protocols.models.RoleTypes
    :param tenant_id: This conversation's tenant ID
    :type tenant_id: str
    :param properties: This conversation's properties
    :type properties: object
    """

    is_group: Optional[bool] = Field(None, alias="isGroup")
    conversation_type: Optional[NonEmptyString] = Field(None, alias="conversationType")
    id: Optional[NonEmptyString] = Field(None, alias="id")
    name: Optional[NonEmptyString] = Field(None, alias="name")
    aad_object_id: Optional[NonEmptyString] = Field(None, alias="aadObjectId")
    role: Optional[NonEmptyString] = Field(None, alias="role")
    tenant_id: Optional[NonEmptyString] = Field(None, alias="tenantID")
    properties: Optional[object] = Field(None, alias="properties")
