from pydantic import BaseModel, Field


class Thing(BaseModel):
    """Thing (entity type: "https://schema.org/Thing").

    :param type: The type of the thing
    :type type: str
    :param name: The name of the thing
    :type name: str
    """

    type: str = Field(None, alias="type")
    name: str = Field(None, alias="name")
