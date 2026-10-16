from enum import Enum


class CurrencyHolderType(str, Enum):
    GROUP = "Group"
    UNDEFINED = "Undefined"
    USER = "User"
    USERKEY = "UserKey"

    def __str__(self) -> str:
        return str(self.value)
