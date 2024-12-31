from pydantic import BaseModel, Field
from .thumbnail_url import ThumbnailUrl
from .media_url import MediaUrl
from .card_action import CardAction


class MediaCard(BaseModel):
    """Media card.

    :param title: Title of this card
    :type title: str
    :param subtitle: Subtitle of this card
    :type subtitle: str
    :param text: Text of this card
    :type text: str
    :param image: Thumbnail placeholder
    :type image: ~microsoft.agents.protocols.models.ThumbnailUrl
    :param media: Media URLs for this card. When this field contains more than
     one URL, each URL is an alternative format of the same content.
    :type media: list[~microsoft.agents.protocols.models.MediaUrl]
    :param buttons: Actions on this card
    :type buttons: list[~microsoft.agents.protocols.models.CardAction]
    :param shareable: This content may be shared with others (default:true)
    :type shareable: bool
    :param autoloop: Should the client loop playback at end of content
     (default:true)
    :type autoloop: bool
    :param autostart: Should the client automatically start playback of media
     in this card (default:true)
    :type autostart: bool
    :param aspect: Aspect ratio of thumbnail/media placeholder. Allowed values
     are "16:9" and "4:3"
    :type aspect: str
    :param duration: Describes the length of the media content without
     requiring a receiver to open the content. Formatted as an ISO 8601
     Duration field.
    :type duration: str
    :param value: Supplementary parameter for this card
    :type value: object
    """

    title: str = Field(None, alias="title")
    subtitle: str = Field(None, alias="subtitle")
    text: str = Field(None, alias="text")
    image: ThumbnailUrl = Field(None, alias="image")
    media: list[MediaUrl] = Field(None, alias="media")
    buttons: list[CardAction] = Field(None, alias="buttons")
    shareable: bool = Field(None, alias="shareable")
    autoloop: bool = Field(None, alias="autoloop")
    autostart: bool = Field(None, alias="autostart")
    aspect: str = Field(None, alias="aspect")
    duration: str = Field(None, alias="duration")
    value: object = Field(None, alias="value")
