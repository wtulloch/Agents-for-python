from pydantic import BaseModel, Field
from typing import Optional
from .thumbnail_url import ThumbnailUrl
from .media_url import MediaUrl
from .card_action import CardAction
from ._type_aliases import NonEmptyString


class VideoCard(BaseModel):
    """Video card.

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

    title: Optional[NonEmptyString] = Field(None, alias="title")
    subtitle: Optional[NonEmptyString] = Field(None, alias="subtitle")
    text: Optional[NonEmptyString] = Field(None, alias="text")
    image: Optional[ThumbnailUrl] = Field(None, alias="image")
    media: Optional[list[MediaUrl]] = Field(None, alias="media")
    buttons: Optional[list[CardAction]] = Field(None, alias="buttons")
    shareable: Optional[bool] = Field(None, alias="shareable")
    autoloop: Optional[bool] = Field(None, alias="autoloop")
    autostart: Optional[bool] = Field(None, alias="autostart")
    aspect: Optional[NonEmptyString] = Field(None, alias="aspect")
    duration: Optional[NonEmptyString] = Field(None, alias="duration")
    value: Optional[object] = Field(None, alias="value")
