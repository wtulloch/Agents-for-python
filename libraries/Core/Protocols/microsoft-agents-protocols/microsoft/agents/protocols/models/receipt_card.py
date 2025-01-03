from pydantic import BaseModel, Field
from .fact import Fact
from .receipt_item import ReceiptItem
from .card_action import CardAction
from ._type_aliases import NonEmptyString
from typing import Optional


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

    title: Optional[NonEmptyString] = Field(None, alias="title")
    facts: Optional[list[Fact]] = Field(None, alias="facts")
    items: Optional[list[ReceiptItem]] = Field(None, alias="items")
    tap: Optional[CardAction] = Field(None, alias="tap")
    total: Optional[NonEmptyString] = Field(None, alias="total")
    tax: Optional[NonEmptyString] = Field(None, alias="tax")
    vat: Optional[NonEmptyString] = Field(None, alias="vat")
    buttons: Optional[list[CardAction]] = Field(None, alias="buttons")
