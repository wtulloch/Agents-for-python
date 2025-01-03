# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from pydantic import BaseModel, Field
from ._type_aliases import NonEmptyString
from typing import Optional


class TokenResponse(BaseModel):
    """A response that includes a user token.

    :param connection_name: The connection name
    :type connection_name: str
    :param token: The user token
    :type token: str
    :param expiration: Expiration for the token, in ISO 8601 format (e.g.
     "2007-04-05T14:30Z")
    :type expiration: str
    :param channel_id: The channelId of the TokenResponse
    :type channel_id: str
    """

    connection_name: Optional[NonEmptyString] = Field(None, alias="connectionName")
    token: Optional[NonEmptyString] = Field(None, alias="token")
    expiration: Optional[NonEmptyString] = Field(None, alias="expiration")
    channel_id: Optional[NonEmptyString] = Field(None, alias="channelId")
