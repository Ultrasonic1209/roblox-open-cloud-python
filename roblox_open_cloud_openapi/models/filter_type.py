from enum import StrEnum


class FilterType(StrEnum):
    NUMBER = "Number"
    STRING = "String"

    def __str__(self) -> str:
        return str(self.value)
