from pydantic import BaseModel

from ._type_aliases import NonEmptyString

class TokenPostResource(BaseModel):
    """
    A type containing information for token posting.
    """

    sas_url: NonEmptyString = None
