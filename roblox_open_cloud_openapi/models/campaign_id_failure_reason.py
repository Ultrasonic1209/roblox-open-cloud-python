from enum import StrEnum


class CampaignIDFailureReason(StrEnum):
    NOT_FOUND = "NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
