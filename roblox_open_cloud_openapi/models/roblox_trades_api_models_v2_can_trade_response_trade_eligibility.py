from enum import Enum


class RobloxTradesApiModelsV2CanTradeResponseTradeEligibility(str, Enum):
    ELIGIBLE = "Eligible"
    INELIGIBLECANNOTTRADEWITHROBLOX = "IneligibleCannotTradeWithRoblox"
    INELIGIBLELEGALORREGULATORYRESTRICTIONS = "IneligibleLegalOrRegulatoryRestrictions"
    INELIGIBLEMISSINGPREMIUMMEMBERSHIP = "IneligibleMissingPremiumMembership"
    INELIGIBLETRADESYSTEMDISABLED = "IneligibleTradeSystemDisabled"
    INELIGIBLEUSERNOTFOUND = "IneligibleUserNotFound"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
