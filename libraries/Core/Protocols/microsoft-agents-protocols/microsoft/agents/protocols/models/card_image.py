from pydantic import BaseModel, Field
from .card_action import CardAction


class CardImage(BaseModel):
    """An image on a card.

    :param url: URL thumbnail image for major content property
    :type url: str
    :param alt: Image description intended for screen readers
    :type alt: str
    :param tap: Action assigned to specific Attachment
    :type tap: ~microsoft.agents.protocols.models.CardAction
    """

    url: str = Field(None, alias="url")
    alt: str = Field(None, alias="alt")
    tap: CardAction = Field(None, alias="tap")
