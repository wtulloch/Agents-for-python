from pydantic import BaseModel, Field


class AttachmentView(BaseModel):
    """Attachment View name and size.

    :param view_id: Id of the attachment
    :type view_id: str
    :param size: Size of the attachment
    :type size: int
    """

    view_id: str = Field(None, alias="viewId")
    size: int = Field(None, alias="size")
