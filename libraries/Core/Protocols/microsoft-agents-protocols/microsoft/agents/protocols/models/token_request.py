from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class TokenRequest(BaseModel):
    """A request to receive a user token.

    :param provider: The provider to request a user token from
    :type provider: str
    :param settings: A collection of settings for the specific provider for
     this request
    :type settings: dict[str, object]
    """

    provider: Optional[NonEmptyString] = Field(None, alias="provider")
    settings: Optional[dict] = Field(None, alias="settings")
