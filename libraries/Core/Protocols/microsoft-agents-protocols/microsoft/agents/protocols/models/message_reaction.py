from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class MessageReaction(BaseModel):
    """Message reaction object.

    :param type: Message reaction type. Possible values include: 'like',
     'plusOne'
    :type type: str or ~microsoft.agents.protocols.models.MessageReactionTypes
    """

    type: Optional[NonEmptyString] = Field(None, alias="type")
