from enum import Enum


class GetV1UniversesUniverseIdBadgesSortBy(str, Enum):
    DATECREATED = "DateCreated"
    RANK = "Rank"

    def __str__(self) -> str:
        return str(self.value)
