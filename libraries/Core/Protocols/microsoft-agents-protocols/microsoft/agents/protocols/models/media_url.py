from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class MediaUrl(BaseModel):
    """Media URL.

    :param url: Url for the media
    :type url: str
    :param profile: Optional profile hint to the client to differentiate
     multiple MediaUrl objects from each other
    :type profile: str
    """

    url: Optional[NonEmptyString] = Field(None, alias="url")
    profile: Optional[NonEmptyString] = Field(None, alias="profile")
