from pydantic import BaseModel, Field


class AttachmentData(BaseModel):
    """Attachment data.

    :param type: Content-Type of the attachment
    :type type: str
    :param name: Name of the attachment
    :type name: str
    :param original_base64: Attachment content
    :type original_base64: bytearray
    :param thumbnail_base64: Attachment thumbnail
    :type thumbnail_base64: bytearray
    """

    type: str = Field(None, alias="type")
    name: str = Field(None, alias="name")
    original_base64: bytearray = Field(None, alias="originalBase64")
    thumbnail_base64: bytearray = Field(None, alias="thumbnailBase64")
