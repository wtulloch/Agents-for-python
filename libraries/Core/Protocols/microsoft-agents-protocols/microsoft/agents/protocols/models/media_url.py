from pydantic import BaseModel, Field


class MediaUrl(BaseModel):
    """Media URL.

    :param url: Url for the media
    :type url: str
    :param profile: Optional profile hint to the client to differentiate
     multiple MediaUrl objects from each other
    :type profile: str
    """

    url: str = Field(None, alias="url")
    profile: str = Field(None, alias="profile")
