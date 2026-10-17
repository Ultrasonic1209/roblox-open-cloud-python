from enum import StrEnum


class SortDirection(StrEnum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
