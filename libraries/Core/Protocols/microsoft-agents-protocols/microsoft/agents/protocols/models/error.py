from pydantic import BaseModel, Field
from typing import Optional
from .inner_http_error import InnerHttpError
from ._type_aliases import NonEmptyString


class Error(BaseModel):
    """Object representing error information.

    :param code: Error code
    :type code: str
    :param message: Error message
    :type message: str
    :param inner_http_error: Error from inner http call
    :type inner_http_error: ~microsoft.agents.protocols.models.InnerHttpError
    """

    code: Optional[NonEmptyString] = Field(None, alias="code")
    message: Optional[NonEmptyString] = Field(None, alias="message")
    inner_http_error: Optional[InnerHttpError] = Field(None, alias="innerHttpError")
