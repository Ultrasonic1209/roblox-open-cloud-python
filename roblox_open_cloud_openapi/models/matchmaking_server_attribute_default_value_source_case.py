from enum import Enum


class MatchmakingServerAttributeDefaultValueSourceCase(str, Enum):
    CONSTANT = "Constant"
    INVALID = "Invalid"
    PLAYERATTRIBUTEREFERENCE = "PlayerAttributeReference"

    def __str__(self) -> str:
        return str(self.value)
