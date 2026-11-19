from enum import StrEnum


class FilterField(StrEnum):
    ALL = "ALL"
    ENGINEVERSION = "EngineVersion"
    PLACEVERSION = "PlaceVersion"
    SERVERREGION = "ServerRegion"

    def __str__(self) -> str:
        return str(self.value)
