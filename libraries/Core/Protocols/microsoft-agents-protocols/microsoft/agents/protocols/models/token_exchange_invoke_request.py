from pydantic import BaseModel, Field
from ._type_aliases import NonEmptyString
from typing import Optional


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

    id: Optional[NonEmptyString] = Field(None, alias="id")
    connection_name: Optional[NonEmptyString] = Field(None, alias="connectionName")
    token: Optional[NonEmptyString] = Field(None, alias="token")
    properties: Optional[dict] = Field(None, alias="properties")
