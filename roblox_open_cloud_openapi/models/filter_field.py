from enum import Enum


class FilterField(str, Enum):
    ALL = "ALL"
    ENGINEVERSION = "EngineVersion"
    PLACEVERSION = "PlaceVersion"

    def __str__(self) -> str:
        return str(self.value)
