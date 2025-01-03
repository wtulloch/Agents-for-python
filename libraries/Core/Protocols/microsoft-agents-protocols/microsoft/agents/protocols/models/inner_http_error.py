from pydantic import BaseModel, Field
from typing import Optional


class InnerHttpError(BaseModel):
    """Object representing inner http error.

    :param status_code: HttpStatusCode from failed request
    :type status_code: int
    :param body: Body from failed request
    :type body: object
    """

    status_code: Optional[int] = Field(None, alias="statusCode")
    body: Optional[object] = Field(None, alias="body")
