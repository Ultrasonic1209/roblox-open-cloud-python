from enum import Enum


class SortDirection(str, Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
