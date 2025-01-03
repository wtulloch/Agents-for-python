from typing import Optional
from pydantic import BaseModel, Field
from ._type_aliases import NonEmptyString


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

    type: Optional[NonEmptyString] = Field(None, alias="type")
    name: Optional[NonEmptyString] = Field(None, alias="name")
    original_base64: Optional[bytearray] = Field(None, alias="originalBase64")
    thumbnail_base64: Optional[bytearray] = Field(None, alias="thumbnailBase64")
