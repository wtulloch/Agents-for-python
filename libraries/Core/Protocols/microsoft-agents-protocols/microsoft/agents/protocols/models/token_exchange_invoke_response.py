from pydantic import BaseModel, Field
from ._type_aliases import NonEmptyString
from typing import Optional


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

    id: Optional[NonEmptyString] = Field(None, alias="id")
    connection_name: Optional[NonEmptyString] = Field(None, alias="connectionName")
    failure_detail: Optional[NonEmptyString] = Field(None, alias="failureDetail")
    properties: Optional[dict] = Field(None, alias="properties")
