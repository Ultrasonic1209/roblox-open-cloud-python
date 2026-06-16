from enum import Enum


class GetV1UniversesUniverseIdBadgesSortOrder(str, Enum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
