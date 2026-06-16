from enum import Enum


class MatchmakingNumericalAttributeComparisonType(str, Enum):
    ABSOLUTEDIFFERENTTOCONSTANT = "AbsoluteDifferentToConstant"
    ABSOLUTEDIFFERENTTOPLAYER = "AbsoluteDifferentToPlayer"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
