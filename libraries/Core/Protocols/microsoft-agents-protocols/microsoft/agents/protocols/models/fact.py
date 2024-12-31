from pydantic import BaseModel, Field


class Fact(BaseModel):
    """Set of key-value pairs. Advantage of this section is that key and value
    properties will be
    rendered with default style information with some delimiter between them.
    So there is no need for developer to specify style information.

    :param key: The key for this Fact
    :type key: str
    :param value: The value for this Fact
    :type value: str
    """

    key: str = Field(None, alias="key")
    value: str = Field(None, alias="value")
