from enum import Enum


class RobloxTradesApiModelsV2CanTradeWithResponseMutualTradeEligibility(str, Enum):
    CALLINGUSERINELIGIBLE = "CallingUserIneligible"
    CALLINGUSERPRIVACYSETTINGSRESTRICTED = "CallingUserPrivacySettingsRestricted"
    CANNOTTRADEWITHSELF = "CannotTradeWithSelf"
    ELIGIBLE = "Eligible"
    TARGETUSERINELIGIBLE = "TargetUserIneligible"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
