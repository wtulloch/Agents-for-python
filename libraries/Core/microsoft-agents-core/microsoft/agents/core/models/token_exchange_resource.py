from pydantic import BaseModel

from ._type_aliases import NonEmptyString


class TokenExchangeResource(BaseModel):
    """
    A type containing information for token exchange.
    """

    id: NonEmptyString = None
    uri: NonEmptyString = None
    provider_id: NonEmptyString = None
