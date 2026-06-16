from enum import Enum


class GetV1UniversesUniverseIdStatsType(str, Enum):
    PREMIUMUPSELLS = "PremiumUpsells"
    PREMIUMVISITS = "PremiumVisits"

    def __str__(self) -> str:
        return str(self.value)
