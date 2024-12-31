from pydantic import BaseModel, Field
from .inner_http_error import InnerHttpError


class Error(BaseModel):
    """Object representing error information.

    :param code: Error code
    :type code: str
    :param message: Error message
    :type message: str
    :param inner_http_error: Error from inner http call
    :type inner_http_error: ~microsoft.agents.protocols.models.InnerHttpError
    """

    code: str = Field(None, alias="code")
    message: str = Field(None, alias="message")
    inner_http_error: InnerHttpError = Field(None, alias="innerHttpError")
