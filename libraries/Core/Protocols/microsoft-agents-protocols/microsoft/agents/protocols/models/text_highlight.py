from pydantic import BaseModel, Field


class TextHighlight(BaseModel):
    """Refers to a substring of content within another field.

    :param text: Defines the snippet of text to highlight
    :type text: str
    :param occurrence: Occurrence of the text field within the referenced
     text, if multiple exist.
    :type occurrence: int
    """

    text: str = Field(None, alias="text")
    occurrence: int = Field(None, alias="occurrence")
