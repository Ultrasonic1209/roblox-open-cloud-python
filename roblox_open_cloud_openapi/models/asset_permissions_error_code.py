from enum import Enum


class AssetPermissionsErrorCode(str, Enum):
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
    REQUESTERNOTCONNECTED = "RequesterNotConnected"
    REQUESTNOTFOUND = "RequestNotFound"
    SUBJECTNOTFOUND = "SubjectNotFound"
    UNKNOWNERROR = "UnknownError"

    def __str__(self) -> str:
        return str(self.value)
