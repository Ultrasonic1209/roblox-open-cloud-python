from enum import StrEnum


class GetV1UniversesUniverseIdStatsType(StrEnum):
    PREMIUMUPSELLS = "PremiumUpsells"
    PREMIUMVISITS = "PremiumVisits"

    def __str__(self) -> str:
        return str(self.value)
