from pydantic import BaseModel, Field
from .attachment_view import AttachmentView


class AttachmentInfo(BaseModel):
    """Metadata for an attachment.

    :param name: Name of the attachment
    :type name: str
    :param type: ContentType of the attachment
    :type type: str
    :param views: attachment views
    :type views: list[~microsoft.agents.protocols.models.AttachmentView]
    """

    name: str = Field(None, alias="name")
    type: str = Field(None, alias="type")
    views: list[AttachmentView] = Field(None, alias="views")
