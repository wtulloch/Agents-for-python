from typing import Optional
from pydantic import BaseModel, Field
from ._type_aliases import NonEmptyString


class AttachmentView(BaseModel):
    """Attachment View name and size.

    :param view_id: Id of the attachment
    :type view_id: str
    :param size: Size of the attachment
    :type size: int
    """

    view_id: Optional[NonEmptyString] = Field(None, alias="viewId")
    size: Optional[int] = Field(None, alias="size")
