from pydantic import BaseModel, Field
from .card_image import CardImage
from .card_action import CardAction


class ThumbnailCard(BaseModel):
    """A thumbnail card (card with a single, small thumbnail image).

    :param title: Title of the card
    :type title: str
    :param subtitle: Subtitle of the card
    :type subtitle: str
    :param text: Text for the card
    :type text: str
    :param images: Array of images for the card
    :type images: list[~microsoft.agents.protocols.models.CardImage]
    :param buttons: Set of actions applicable to the current card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    :param tap: This action will be activated when user taps on the card
     itself
    :type tap: ~microsoft.agents.protocols.models.CardAction
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    images: list[CardImage] = Field(None, alias="images")
    buttons: list[CardAction] = Field(None, alias="buttons")
    tap: CardAction = Field(None, alias="tap")
