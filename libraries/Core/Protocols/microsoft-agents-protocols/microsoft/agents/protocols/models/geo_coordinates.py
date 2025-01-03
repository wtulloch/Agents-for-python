from pydantic import BaseModel, Field
from typing import Optional
from ._type_aliases import NonEmptyString


class GeoCoordinates(BaseModel):
    """GeoCoordinates (entity type: "https://schema.org/GeoCoordinates").

    :param elevation: Elevation of the location [WGS
     84](https://en.wikipedia.org/wiki/World_Geodetic_System)
    :type elevation: float
    :param latitude: Latitude of the location [WGS
     84](https://en.wikipedia.org/wiki/World_Geodetic_System)
    :type latitude: float
    :param longitude: Longitude of the location [WGS
     84](https://en.wikipedia.org/wiki/World_Geodetic_System)
    :type longitude: float
    :param type: The type of the thing
    :type type: str
    :param name: The name of the thing
    :type name: str
    """

    elevation: Optional[float] = Field(None, alias="elevation")
    latitude: Optional[float] = Field(None, alias="latitude")
    longitude: Optional[float] = Field(None, alias="longitude")
    type: Optional[NonEmptyString] = Field(None, alias="type")
    name: Optional[NonEmptyString] = Field(None, alias="name")
