from enum import Enum


class RobloxLocalizationTablesApiCursorEntryIdentifierSortOrder(str, Enum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
