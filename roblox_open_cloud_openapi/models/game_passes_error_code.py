from enum import Enum


class GamePassesErrorCode(str, Enum):
    ACTIVEINPO = "ActiveInPO"
    ASSETCREATIONFAILURE = "AssetCreationFailure"
    ASSETNOTFOUND = "AssetNotFound"
    BADREQUEST = "BadRequest"
    BLOCKED = "Blocked"
    COMMISSIONRATENOTFOUND = "CommissionRateNotFound"
    FILETOOLARGE = "FileTooLarge"
    INTERNALERROR = "InternalError"
    INVALIDCOUNT = "InvalidCount"
    INVALIDPAGESIZE = "InvalidPageSize"
    MISSINGARGUMENT = "MissingArgument"
    NOTAUTHENTICATED = "NotAuthenticated"
    NOTFORSALE = "NotForSale"
    NOTFOUND = "NotFound"
    NOTSAMEUNIVERSE = "NotSameUniverse"
    PASSALREADYREVOKED = "PassAlreadyRevoked"
    PASSNOTFOUND = "PassNotFound"
    PASSREVOKEFAILURE = "PassRevokeFailure"
    PRICINGCONFIGERROR = "PricingConfigError"
    SALESNOTFOUND = "SalesNotFound"
    TARGETUNAUTHORIZEDACCESS = "TargetUnauthorizedAccess"
    UNAUTHORIZEDACCESS = "UnauthorizedAccess"
    UNIVERSENOTFOUND = "UniverseNotFound"

    def __str__(self) -> str:
        return str(self.value)
