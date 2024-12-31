from pydantic import BaseModel, Field


class TokenExchangeInvokeRequest(BaseModel):
    """TokenExchangeInvokeRequest.

    :param id: The id from the OAuthCard.
    :type id: str
    :param connection_name: The connection name.
    :type connection_name: str
    :param token: The user token that can be exchanged.
    :type token: str
    :param properties: Extension data for overflow of properties.
    :type properties: dict[str, object]
    """

    id: str = Field(None, alias="id")
    connection_name: str = Field(None, alias="connectionName")
    token: str = Field(None, alias="token")
    properties: dict = Field(None, alias="properties")
