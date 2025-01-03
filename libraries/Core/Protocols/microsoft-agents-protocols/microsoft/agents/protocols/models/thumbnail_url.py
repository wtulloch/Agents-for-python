from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class ThumbnailUrl(BaseModel):
    """Thumbnail URL.

    :param url: URL pointing to the thumbnail to use for media content
    :type url: str
    :param alt: HTML alt text to include on this thumbnail image
    :type alt: str
    """

    url: Optional[NonEmptyString] = Field(None, alias="url")
    alt: Optional[NonEmptyString] = Field(None, alias="alt")
