from pydantic import BaseModel, Field
from typing import Optional
from .card_action import CardAction
from ._type_aliases import NonEmptyString


class CardImage(BaseModel):
    """An image on a card.

    :param url: URL thumbnail image for major content property
    :type url: str
    :param alt: Image description intended for screen readers
    :type alt: str
    :param tap: Action assigned to specific Attachment
    :type tap: ~microsoft.agents.protocols.models.CardAction
    """

    url: Optional[NonEmptyString] = Field(None, alias="url")
    alt: Optional[NonEmptyString] = Field(None, alias="alt")
    tap: Optional[CardAction] = Field(None, alias="tap")
