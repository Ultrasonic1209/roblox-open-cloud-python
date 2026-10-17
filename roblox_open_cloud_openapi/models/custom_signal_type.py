from enum import StrEnum


class CustomSignalType(StrEnum):
    INVALID = "Invalid"
    PLAYERCATEGORICAL = "PlayerCategorical"
    PLAYERNUMERICAL = "PlayerNumerical"
    SERVERCATEGORICAL = "ServerCategorical"
    SERVERNUMERICAL = "ServerNumerical"

    def __str__(self) -> str:
        return str(self.value)
