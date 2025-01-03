from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class Thing(BaseModel):
    """Thing (entity type: "https://schema.org/Thing").

    :param type: The type of the thing
    :type type: str
    :param name: The name of the thing
    :type name: str
    """

    type: Optional[NonEmptyString] = Field(None, alias="type")
    name: Optional[NonEmptyString] = Field(None, alias="name")
