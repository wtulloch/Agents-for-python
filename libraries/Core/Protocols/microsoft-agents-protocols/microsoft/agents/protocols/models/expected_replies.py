from pydantic import BaseModel, Field
from .activity import Activity


class ExpectedReplies(BaseModel):
    """ExpectedReplies.

    :param activities: A collection of Activities that conforms to the
     ExpectedReplies schema.
    :type activities: list[~microsoft.agents.protocols.models.Activity]
    """

    activities: list[Activity] = Field(None, alias="activities")
