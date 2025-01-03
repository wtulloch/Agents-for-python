from typing import Optional
from pydantic import BaseModel, Field
from ._type_aliases import NonEmptyString


class AdaptiveCardInvokeResponse(BaseModel):
    """AdaptiveCardInvokeResponse.

    Defines the structure that is returned as the result of an Invoke activity with Name of 'adaptiveCard/action'.

    :param status_code: The Card Action Response StatusCode.
    :type status_code: int
    :param type: The type of this Card Action Response.
    :type type: str
    :param value: The JSON response object.
    :type value: dict[str, object]
    """

    status_code: Optional[int] = Field(None, alias="statusCode")
    type: Optional[NonEmptyString] = Field(None, alias="type")
    value: Optional[dict[NonEmptyString, object]] = Field(None, alias="value")
