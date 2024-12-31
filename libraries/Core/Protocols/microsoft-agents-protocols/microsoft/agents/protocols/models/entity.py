from pydantic import BaseModel, Field


class Entity(BaseModel):
    """Metadata object pertaining to an activity.

    :param type: Type of this entity (RFC 3987 IRI)
    :type type: str
    """

    type: str = Field(None, alias="type")
