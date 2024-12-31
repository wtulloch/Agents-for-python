from pydantic import BaseModel, Field


class MediaEventValue(BaseModel):
    """Supplementary parameter for media events.

    :param card_value: Callback parameter specified in the Value field of the
     MediaCard that originated this event
    :type card_value: object
    """

    card_value: object = Field(None, alias="cardValue")
