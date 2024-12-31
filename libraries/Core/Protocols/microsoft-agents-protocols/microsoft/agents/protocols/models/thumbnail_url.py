from pydantic import BaseModel, Field


class ThumbnailUrl(BaseModel):
    """Thumbnail URL.

    :param url: URL pointing to the thumbnail to use for media content
    :type url: str
    :param alt: HTML alt text to include on this thumbnail image
    :type alt: str
    """

    url: str = Field(None, alias="url")
    alt: str = Field(None, alias="alt")
