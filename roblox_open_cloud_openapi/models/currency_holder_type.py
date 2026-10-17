from enum import StrEnum


class CurrencyHolderType(StrEnum):
    GROUP = "Group"
    UNDEFINED = "Undefined"
    USER = "User"
    USERKEY = "UserKey"

    def __str__(self) -> str:
        return str(self.value)
