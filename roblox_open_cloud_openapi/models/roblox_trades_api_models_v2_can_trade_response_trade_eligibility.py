from enum import Enum


class RobloxTradesApiModelsV2CanTradeResponseTradeEligibility(str, Enum):
    ELIGIBLE = "Eligible"
    INELIGIBLEAGECHECKREQUIRED = "IneligibleAgeCheckRequired"
    INELIGIBLECANNOTTRADEWITHROBLOX = "IneligibleCannotTradeWithRoblox"
    INELIGIBLEFREETRADESLIMITREACHED = "IneligibleFreeTradesLimitReached"
    INELIGIBLELEGALORREGULATORYRESTRICTIONS = "IneligibleLegalOrRegulatoryRestrictions"
    INELIGIBLEMISSINGPREMIUMMEMBERSHIP = "IneligibleMissingPremiumMembership"
    INELIGIBLETRADESYSTEMDISABLED = "IneligibleTradeSystemDisabled"
    INELIGIBLEUSERNOTFOUND = "IneligibleUserNotFound"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
