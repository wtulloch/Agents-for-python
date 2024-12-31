from pydantic import BaseModel, Field
from .fact import Fact
from .receipt_item import ReceiptItem
from .card_action import CardAction


class ReceiptCard(BaseModel):
    """A receipt card.

    :param title: Title of the card
    :type title: str
    :param facts: Array of Fact objects
    :type facts: list[~microsoft.agents.protocols.models.Fact]
    :param items: Array of Receipt Items
    :type items: list[~microsoft.agents.protocols.models.ReceiptItem]
    :param tap: This action will be activated when user taps on the card
    :type tap: ~microsoft.agents.protocols.models.CardAction
    :param total: Total amount of money paid (or to be paid)
    :type total: str
    :param tax: Total amount of tax paid (or to be paid)
    :type tax: str
    :param vat: Total amount of VAT paid (or to be paid)
    :type vat: str
    :param buttons: Set of actions applicable to the current card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    """

    title: str = Field(None, alias="title")
    facts: list[Fact] = Field(None, alias="facts")
    items: list[ReceiptItem] = Field(None, alias="items")
    tap: CardAction = Field(None, alias="tap")
    total: str = Field(None, alias="total")
    tax: str = Field(None, alias="tax")
    vat: str = Field(None, alias="vat")
    buttons: list[CardAction] = Field(None, alias="buttons")
