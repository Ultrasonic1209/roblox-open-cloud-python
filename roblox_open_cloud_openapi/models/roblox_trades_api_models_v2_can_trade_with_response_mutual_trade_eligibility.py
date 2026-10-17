from enum import StrEnum


class RobloxTradesApiModelsV2CanTradeWithResponseMutualTradeEligibility(StrEnum):
    CALLINGUSERAGECHECKREQUIRED = "CallingUserAgeCheckRequired"
    CALLINGUSERINELIGIBLE = "CallingUserIneligible"
    CALLINGUSERPRIVACYSETTINGSRESTRICTED = "CallingUserPrivacySettingsRestricted"
    CANNOTTRADEWITHSELF = "CannotTradeWithSelf"
    ELIGIBLE = "Eligible"
    TARGETUSERINELIGIBLE = "TargetUserIneligible"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
