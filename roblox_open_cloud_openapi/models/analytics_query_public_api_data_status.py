from enum import Enum


class AnalyticsQueryPublicApiDataStatus(str, Enum):
    NOTSTATISTICALLYSIGNIFICANT = "NotStatisticallySignificant"
    PROJECTED = "Projected"
    VALID = "Valid"

    def __str__(self) -> str:
        return str(self.value)
