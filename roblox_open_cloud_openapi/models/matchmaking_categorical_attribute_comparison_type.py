from enum import Enum


class MatchmakingCategoricalAttributeComparisonType(str, Enum):
    EQUALITYTOCONSTANT = "EqualityToConstant"
    EQUALITYTOPLAYER = "EqualityToPlayer"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
