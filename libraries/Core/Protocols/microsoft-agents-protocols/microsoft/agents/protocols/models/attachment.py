from typing import Optional
from pydantic import BaseModel, Field
from ._type_aliases import NonEmptyString


class Attachment(BaseModel):
    """An attachment within an activity.

    :param content_type: mimetype/Contenttype for the file
    :type content_type: str
    :param content_url: Content Url
    :type content_url: str
    :param content: Embedded content
    :type content: object
    :param name: (OPTIONAL) The name of the attachment
    :type name: str
    :param thumbnail_url: (OPTIONAL) Thumbnail associated with attachment
    :type thumbnail_url: str
    """

    content_type: NonEmptyString = Field(None, alias="contentType")
    content_url: Optional[NonEmptyString] = Field(None, alias="contentUrl")
    content: Optional[object] = Field(None, alias="content")
    name: Optional[NonEmptyString] = Field(None, alias="name")
    thumbnail_url: Optional[NonEmptyString] = Field(None, alias="thumbnailUrl")
