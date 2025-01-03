from pydantic import BaseModel, Field
from typing import Optional


class MediaEventValue(BaseModel):
    """Supplementary parameter for media events.

    :param card_value: Callback parameter specified in the Value field of the
     MediaCard that originated this event
    :type card_value: object
    """

    card_value: Optional[object] = Field(None, alias="cardValue")
