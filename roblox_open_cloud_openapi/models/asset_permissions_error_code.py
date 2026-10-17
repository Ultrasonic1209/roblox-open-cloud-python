from enum import StrEnum


class AssetPermissionsErrorCode(StrEnum):
    ALREADYHASACCESS = "AlreadyHasAccess"
    ALREADYPENDING = "AlreadyPending"
    ASSETNOTFOUND = "AssetNotFound"
    ASSETTYPENOTENABLED = "AssetTypeNotEnabled"
    BATCHSIZELIMITEXCEEDED = "BatchSizeLimitExceeded"
    CALLERNOTOWNER = "CallerNotOwner"
    CANNOTMANAGEASSET = "CannotManageAsset"
    CANNOTMANAGESUBJECT = "CannotManageSubject"
    DEPENDENCIESLIMITREACHED = "DependenciesLimitReached"
    INVALIDREQUEST = "InvalidRequest"
    INVALIDREQUESTSTATUS = "InvalidRequestStatus"
    NOTREQUESTABLE = "NotRequestable"
    PERMISSIONLIMITREACHED = "PermissionLimitReached"
    PUBLICASSETCANNOTBEGRANTEDTO = "PublicAssetCannotBeGrantedTo"
    RATELIMITED = "RateLimited"
    REQUESTERNOTACONNECTION = "RequesterNotAConnection"
    REQUESTNOTFOUND = "RequestNotFound"
    SUBJECTNOTFOUND = "SubjectNotFound"
    UNKNOWNERROR = "UnknownError"

    def __str__(self) -> str:
        return str(self.value)
