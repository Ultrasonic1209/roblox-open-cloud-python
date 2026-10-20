from enum import StrEnum


class AnalyticsQueryPublicApiDataStatus(StrEnum):
    NOTSTATISTICALLYSIGNIFICANT = "NotStatisticallySignificant"
    PROJECTED = "Projected"
    VALID = "Valid"

    def __str__(self) -> str:
        return str(self.value)
