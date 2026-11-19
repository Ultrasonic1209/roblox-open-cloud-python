from enum import StrEnum


class RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModelUsersGroupPayoutEligibilityAdditionalProperty(
    StrEnum
):
    ELIGIBLE = "Eligible"
    NOTINGROUP = "NotInGroup"
    PAYOUTRESTRICTED = "PayoutRestricted"
    UNDEFINED = "Undefined"

    def __str__(self) -> str:
        return str(self.value)
