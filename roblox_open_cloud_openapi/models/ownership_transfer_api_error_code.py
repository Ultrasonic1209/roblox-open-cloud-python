from enum import StrEnum


class OwnershipTransferApiErrorCode(StrEnum):
    EMAILNOTVERIFIED = "EmailNotVerified"
    INSUFFICIENTPERMISSION = "InsufficientPermission"
    INTERNALERROR = "InternalError"
    INVALIDGROUPID = "InvalidGroupId"
    INVALIDHOLDID = "InvalidHoldId"
    INVALIDTARGETRELATIONSHIP = "InvalidTargetRelationship"
    INVALIDTRANSFERACTION = "InvalidTransferAction"
    INVALIDUNIVERSEID = "InvalidUniverseId"
    NOGROUPOWNER = "NoGroupOwner"
    UNSUPPORTEDTRANSFER = "UnsupportedTransfer"

    def __str__(self) -> str:
        return str(self.value)
