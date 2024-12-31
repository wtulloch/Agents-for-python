# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from pydantic import BaseModel, Field


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

    connection_name: str = Field(None, alias="connectionName")
    token: str = Field(None, alias="token")
    expiration: str = Field(None, alias="expiration")
    channel_id: str = Field(None, alias="channelId")
