from enum import StrEnum


class MatchmakingNumericalAttributeComparisonType(StrEnum):
    ABSOLUTEDIFFERENTTOCONSTANT = "AbsoluteDifferentToConstant"
    ABSOLUTEDIFFERENTTOPLAYER = "AbsoluteDifferentToPlayer"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
