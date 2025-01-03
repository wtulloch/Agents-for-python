from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class Entity(BaseModel):
    """Metadata object pertaining to an activity.

    :param type: Type of this entity (RFC 3987 IRI)
    :type type: str
    """

    type: Optional[NonEmptyString] = Field(None, alias="type")
