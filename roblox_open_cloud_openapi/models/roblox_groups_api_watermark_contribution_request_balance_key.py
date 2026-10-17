from enum import StrEnum


class RobloxGroupsApiWatermarkContributionRequestBalanceKey(StrEnum):
    O18BOOSTED = "O18Boosted"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
