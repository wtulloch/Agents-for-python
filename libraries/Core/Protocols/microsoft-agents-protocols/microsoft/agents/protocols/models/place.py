from pydantic import BaseModel, Field


class Place(BaseModel):
    """Place (entity type: "https://schema.org/Place").

    :param address: Address of the place (may be `string` or complex object of
     type `PostalAddress`)
    :type address: object
    :param geo: Geo coordinates of the place (may be complex object of type
     `GeoCoordinates` or `GeoShape`)
    :type geo: object
    :param has_map: Map to the place (may be `string` (URL) or complex object
     of type `Map`)
    :type has_map: object
    :param type: The type of the thing
    :type type: str
    :param name: The name of the thing
    :type name: str
    """

    address: object = Field(None, alias="address")
    geo: object = Field(None, alias="geo")
    has_map: object = Field(None, alias="hasMap")
    type: str = Field(None, alias="type")
    name: str = Field(None, alias="name")
