from pydantic import BaseModel, Field


class TokenRequest(BaseModel):
    """A request to receive a user token.

    :param provider: The provider to request a user token from
    :type provider: str
    :param settings: A collection of settings for the specific provider for
     this request
    :type settings: dict[str, object]
    """

    provider: str = Field(None, alias="provider")
    settings: dict = Field(None, alias="settings")
