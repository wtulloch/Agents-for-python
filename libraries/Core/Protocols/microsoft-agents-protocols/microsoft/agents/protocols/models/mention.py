from pydantic import BaseModel, Field
from .channel_account import ChannelAccount
from ._type_aliases import NonEmptyString
from typing import Optional


class Mention(BaseModel):
    """Mention information (entity type: "mention").

    :param mentioned: The mentioned user
    :type mentioned: ~microsoft.agents.protocols.models.ChannelAccount
    :param text: Sub Text which represents the mention (can be null or empty)
    :type text: str
    :param type: Type of this entity (RFC 3987 IRI)
    :type type: str
    """

    mentioned: Optional[ChannelAccount] = Field(None, alias="mentioned")
    text: Optional[NonEmptyString] = Field(None, alias="text")
    type: Optional[NonEmptyString] = Field(None, alias="type")
