from enum import StrEnum


class GetV1UniversesUniverseIdBadgesSortBy(StrEnum):
    DATECREATED = "DateCreated"
    RANK = "Rank"

    def __str__(self) -> str:
        return str(self.value)
