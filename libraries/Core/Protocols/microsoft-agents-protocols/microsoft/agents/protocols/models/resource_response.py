from pydantic import BaseModel, Field


class ResourceResponse(BaseModel):
    """A response containing a resource ID.

    :param id: Id of the resource
    :type id: str
    """

    id: str = Field(None, alias="id")
