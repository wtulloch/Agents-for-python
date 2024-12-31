from pydantic import BaseModel, Field


class CardAction(BaseModel):
    """A clickable action.

    :param type: The type of action implemented by this button. Possible
     values include: 'openUrl', 'imBack', 'postBack', 'playAudio', 'playVideo',
     'showImage', 'downloadFile', 'signin', 'call', 'messageBack'
    :type type: str or ~microsoft.agents.protocols.models.ActionTypes
    :param title: Text description which appears on the button
    :type title: str
    :param image: Image URL which will appear on the button, next to text
     label
    :type image: str
    :param text: Text for this action
    :type text: str
    :param display_text: (Optional) text to display in the chat feed if the
     button is clicked
    :type display_text: str
    :param value: Supplementary parameter for action. Content of this property
     depends on the ActionType
    :type value: object
    :param channel_data: Channel-specific data associated with this action
    :type channel_data: object
    :param image_alt_text: Alternate image text to be used in place of the `image` field
    :type image_alt_text: str
    """

    type: str = Field(None, alias="type")
    title: str = Field(None, alias="title")
    image: str = Field(None, alias="image")
    text: str = Field(None, alias="text")
    display_text: str = Field(None, alias="displayText")
    value: object = Field(None, alias="value")
    channel_data: object = Field(None, alias="channelData")
    image_alt_text: str = Field(None, alias="imageAltText")
