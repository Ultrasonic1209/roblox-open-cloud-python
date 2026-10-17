from enum import StrEnum


class RobloxLocalizationTablesApiGetTableResponseOwnerType(StrEnum):
    GROUP = "Group"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
