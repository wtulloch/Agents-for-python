from pydantic import BaseModel, Field
from typing import Optional
from .activity import Activity


class Transcript(BaseModel):
    """Transcript.

    :param activities: A collection of Activities that conforms to the
     Transcript schema.
    :type activities: list[~microsoft.agents.protocols.models.Activity]
    """

    activities: Optional[list[Activity]] = Field(None, alias="activities")
