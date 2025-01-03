from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class ResourceResponse(BaseModel):
    """A response containing a resource ID.

    :param id: Id of the resource
    :type id: str
    """

    id: Optional[NonEmptyString] = Field(None, alias="id")
