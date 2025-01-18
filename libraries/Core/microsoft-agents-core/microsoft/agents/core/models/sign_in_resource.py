from pydantic import BaseModel

from ._type_aliases import NonEmptyString
from .token_exchange_resource import TokenExchangeResource
from .token_post_resource import TokenPostResource

class SignInResource(BaseModel):
    """
    A type containing information for single sign-on.
    """

    sign_in_link: NonEmptyString = None
    token_exchange_resource: TokenExchangeResource = None
    token_post_resource: TokenPostResource = None