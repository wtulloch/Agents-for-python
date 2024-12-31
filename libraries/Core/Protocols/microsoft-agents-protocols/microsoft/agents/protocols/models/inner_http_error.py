from pydantic import BaseModel, Field


class InnerHttpError(BaseModel):
    """Object representing inner http error.

    :param status_code: HttpStatusCode from failed request
    :type status_code: int
    :param body: Body from failed request
    :type body: object
    """

    status_code: int = Field(None, alias="statusCode")
    body: object = Field(None, alias="body")
