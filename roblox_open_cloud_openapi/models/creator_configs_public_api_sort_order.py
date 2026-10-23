from enum import StrEnum


class CreatorConfigsPublicApiSortOrder(StrEnum):
    ASCENDING = "SORT_ORDER_ASCENDING"
    DESCENDING = "SORT_ORDER_DESCENDING"

    def __str__(self) -> str:
        return str(self.value)
