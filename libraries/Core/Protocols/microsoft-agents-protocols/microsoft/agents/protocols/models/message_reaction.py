from pydantic import BaseModel, Field


class MessageReaction(BaseModel):
    """Message reaction object.

    :param type: Message reaction type. Possible values include: 'like',
     'plusOne'
    :type type: str or ~microsoft.agents.protocols.models.MessageReactionTypes
    """

    type: str = Field(None, alias="type")
