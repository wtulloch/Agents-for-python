from typing import Optional
from pydantic import BaseModel, Field
from .attachment_view import AttachmentView
from ._type_aliases import NonEmptyString


class AttachmentInfo(BaseModel):
    """Metadata for an attachment.

    :param name: Name of the attachment
    :type name: str
    :param type: ContentType of the attachment
    :type type: str
    :param views: attachment views
    :type views: list[~microsoft.agents.protocols.models.AttachmentView]
    """

    name: Optional[NonEmptyString] = Field(None, alias="name")
    type: Optional[NonEmptyString] = Field(None, alias="type")
    views: Optional[list[AttachmentView]] = Field(None, alias="views")
