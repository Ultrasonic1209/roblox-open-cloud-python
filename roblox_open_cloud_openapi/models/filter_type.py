from enum import Enum


class FilterType(str, Enum):
    NUMBER = "Number"
    STRING = "String"

    def __str__(self) -> str:
        return str(self.value)
