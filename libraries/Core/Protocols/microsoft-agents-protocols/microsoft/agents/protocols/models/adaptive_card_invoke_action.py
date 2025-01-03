from typing import Optional
from pydantic import BaseModel, Field
from ._type_aliases import NonEmptyString


class AdaptiveCardInvokeAction(BaseModel):
    """AdaptiveCardInvokeAction.

    Defines the structure that arrives in the Activity.Value.Action for Invoke activity with
    name of 'adaptiveCard/action'.

    :param type: The Type of this Adaptive Card Invoke Action.
    :type type: str
    :param id: The Id of this Adaptive Card Invoke Action.
    :type id: str
    :param verb: The Verb of this Adaptive Card Invoke Action.
    :type verb: str
    :param data: The data of this Adaptive Card Invoke Action.
    :type data: dict[str, object]
    """

    type: Optional[NonEmptyString] = Field(None, alias="type")
    id: Optional[NonEmptyString] = Field(None, alias="id")
    verb: Optional[NonEmptyString] = Field(None, alias="verb")
    data: Optional[dict[NonEmptyString, object]] = Field(None, alias="data")
