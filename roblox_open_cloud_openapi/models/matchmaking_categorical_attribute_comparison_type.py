from enum import StrEnum


class MatchmakingCategoricalAttributeComparisonType(StrEnum):
    EQUALITYTOCONSTANT = "EqualityToConstant"
    EQUALITYTOPLAYER = "EqualityToPlayer"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
