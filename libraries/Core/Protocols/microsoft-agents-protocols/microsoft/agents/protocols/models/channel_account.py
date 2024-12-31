from pydantic import BaseModel, Field


class ChannelAccount(BaseModel):
    """Channel account information needed to route a message.

    :param id: Channel id for the user or bot on this channel (Example:
     joe@smith.com, or @joesmith or 123456)
    :type id: str
    :param name: Display friendly name
    :type name: str
    :param aad_object_id: This account's object ID within Azure Active
     Directory (AAD)
    :type aad_object_id: str
    :param role: Role of the entity behind the account (Example: User, Bot,
     etc.). Possible values include: 'user', 'bot'
    :type role: str or ~microsoft.agents.protocols.models.RoleTypes
    """

    id: str = Field(None, alias="id")
    name: str = Field(None, alias="name")
    aad_object_id: str = Field(None, alias="aadObjectId")
    role: str = Field(None, alias="role")
    properties: object = Field(None, alias="properties")
