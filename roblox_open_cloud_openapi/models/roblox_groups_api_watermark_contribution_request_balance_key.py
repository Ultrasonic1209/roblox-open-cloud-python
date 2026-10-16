from enum import Enum


class RobloxGroupsApiWatermarkContributionRequestBalanceKey(str, Enum):
    O18BOOSTED = "O18Boosted"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
