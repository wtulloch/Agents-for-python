from pydantic import BaseModel, Field
from .error import Error


class ErrorResponse(BaseModel):
    """An HTTP API response.

    :param error: Error message
    :type error: ~microsoft.agents.protocols.models.Error
    """

    error: Error = Field(None, alias="error")
