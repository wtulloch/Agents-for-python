from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class ConversationResourceResponse(BaseModel):
    """A response containing a resource.

    :param activity_id: ID of the Activity (if sent)
    :type activity_id: str
    :param service_url: Service endpoint where operations concerning the
     conversation may be performed
    :type service_url: str
    :param id: Id of the resource
    :type id: str
    """

    activity_id: Optional[NonEmptyString] = Field(None, alias="activityId")
    service_url: Optional[NonEmptyString] = Field(None, alias="serviceUrl")
    id: Optional[NonEmptyString] = Field(None, alias="id")
