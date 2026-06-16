from enum import Enum


class MatchmakingSignalCurveType(str, Enum):
    INVALID = "Invalid"
    NEGATIVELINEAR = "NegativeLinear"
    POSITIVELINEAR = "PositiveLinear"

    def __str__(self) -> str:
        return str(self.value)
