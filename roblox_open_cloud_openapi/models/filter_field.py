from enum import Enum


class FilterField(str, Enum):
    ALL = "ALL"
    ENGINEVERSION = "EngineVersion"

    def __str__(self) -> str:
        return str(self.value)
