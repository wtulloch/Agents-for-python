from pydantic import BaseModel, Field
from ._type_aliases import NonEmptyString
from typing import Optional


class SemanticAction(BaseModel):
    """Represents a reference to a programmatic action.

    :param id: ID of this action
    :type id: str
    :param entities: Entities associated with this action
    :type entities: dict[str, ~microsoft.agents.protocols.models.Entity]
    :param state: State of this action. Allowed values: `start`, `continue`, `done`
    :type state: str or ~microsoft.agents.protocols.models.SemanticActionStates
    """

    id: Optional[NonEmptyString] = Field(None, alias="id")
    entities: Optional[dict] = Field(None, alias="entities")
    state: Optional[NonEmptyString] = Field(None, alias="state")
