from enum import StrEnum


class MatchmakingSignalCurveType(StrEnum):
    INVALID = "Invalid"
    NEGATIVELINEAR = "NegativeLinear"
    POSITIVELINEAR = "PositiveLinear"

    def __str__(self) -> str:
        return str(self.value)
