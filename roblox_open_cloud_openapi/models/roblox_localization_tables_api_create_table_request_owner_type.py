from enum import StrEnum


class RobloxLocalizationTablesApiCreateTableRequestOwnerType(StrEnum):
    GROUP = "Group"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
