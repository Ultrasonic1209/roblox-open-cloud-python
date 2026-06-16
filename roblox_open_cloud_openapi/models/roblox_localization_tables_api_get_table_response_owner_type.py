from enum import Enum


class RobloxLocalizationTablesApiGetTableResponseOwnerType(str, Enum):
    GROUP = "Group"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
