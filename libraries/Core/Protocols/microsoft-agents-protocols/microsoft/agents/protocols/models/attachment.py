from pydantic import BaseModel, Field


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

    content_type: str = Field(None, alias="contentType")
    content_url: str = Field(None, alias="contentUrl")
    content: object = Field(None, alias="content")
    name: str = Field(None, alias="name")
    thumbnail_url: str = Field(None, alias="thumbnailUrl")
