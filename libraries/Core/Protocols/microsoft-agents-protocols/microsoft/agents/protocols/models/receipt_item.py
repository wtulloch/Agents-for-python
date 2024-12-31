from pydantic import BaseModel, Field
from .card_image import CardImage
from .card_action import CardAction


class ReceiptItem(BaseModel):
    """An item on a receipt card.

    :param title: Title of the Card
    :type title: str
    :param subtitle: Subtitle appears just below Title field, differs from
     Title in font styling only
    :type subtitle: str
    :param text: Text field appears just below subtitle, differs from Subtitle
     in font styling only
    :type text: str
    :param image: Image
    :type image: ~microsoft.agents.protocols.models.CardImage
    :param price: Amount with currency
    :type price: str
    :param quantity: Number of items of given kind
    :type quantity: str
    :param tap: This action will be activated when user taps on the Item
     bubble.
    :type tap: ~microsoft.agents.protocols.models.CardAction
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    image: CardImage = Field(None, alias="image")
    price: str = Field(None, alias="price")
    quantity: str = Field(None, alias="quantity")
    tap: CardAction = Field(None, alias="tap")
