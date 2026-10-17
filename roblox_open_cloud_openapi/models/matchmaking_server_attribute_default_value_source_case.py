from enum import StrEnum


class MatchmakingServerAttributeDefaultValueSourceCase(StrEnum):
    CONSTANT = "Constant"
    INVALID = "Invalid"
    PLAYERATTRIBUTEREFERENCE = "PlayerAttributeReference"

    def __str__(self) -> str:
        return str(self.value)
