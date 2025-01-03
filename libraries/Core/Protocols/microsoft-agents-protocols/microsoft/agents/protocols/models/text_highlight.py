from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class TextHighlight(BaseModel):
    """Refers to a substring of content within another field.

    :param text: Defines the snippet of text to highlight
    :type text: str
    :param occurrence: Occurrence of the text field within the referenced
     text, if multiple exist.
    :type occurrence: int
    """

    text: Optional[NonEmptyString] = Field(None, alias="text")
    occurrence: Optional[int] = Field(None, alias="occurrence")
