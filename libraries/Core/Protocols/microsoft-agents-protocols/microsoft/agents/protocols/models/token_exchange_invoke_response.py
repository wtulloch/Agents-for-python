from pydantic import BaseModel, Field


class TokenExchangeInvokeResponse(BaseModel):
    """TokenExchangeInvokeResponse.

    :param id: The id from the OAuthCard.
    :type id: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param failure_detail: The details of why the token exchange failed.
    :type failure_detail: str
    :param properties: Extension data for overflow of properties.
    :type properties: dict[str, object]
    """

    id: str = Field(None, alias="id")
    connection_name: str = Field(None, alias="connectionName")
    failure_detail: str = Field(None, alias="failureDetail")
    properties: dict = Field(None, alias="properties")
