from pydantic import BaseModel, Field


class SemanticAction(BaseModel):
    """Represents a reference to a programmatic action.

    :param id: ID of this action
    :type id: str
    :param entities: Entities associated with this action
    :type entities: dict[str, ~microsoft.agents.protocols.models.Entity]
    :param state: State of this action. Allowed values: `start`, `continue`, `done`
    :type state: str or ~microsoft.agents.protocols.models.SemanticActionStates
    """

    id: str = Field(None, alias="id")
    entities: dict = Field(None, alias="entities")
    state: str = Field(None, alias="state")
