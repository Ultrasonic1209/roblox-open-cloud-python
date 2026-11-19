from enum import StrEnum


class CampaignRecommendationResponseBudgetType(StrEnum):
    DAILY = "DAILY"

    def __str__(self) -> str:
        return str(self.value)
