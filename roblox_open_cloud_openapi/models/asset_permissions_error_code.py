from enum import Enum


class AssetPermissionsErrorCode(str, Enum):
    ASSETNOTFOUND = "AssetNotFound"
    ASSETTYPENOTENABLED = "AssetTypeNotEnabled"
    CANNOTMANAGEASSET = "CannotManageAsset"
    CANNOTMANAGESUBJECT = "CannotManageSubject"
    DEPENDENCIESLIMITREACHED = "DependenciesLimitReached"
    INVALIDREQUEST = "InvalidRequest"
    PERMISSIONLIMITREACHED = "PermissionLimitReached"
    PUBLICASSETCANNOTBEGRANTEDTO = "PublicAssetCannotBeGrantedTo"
    SUBJECTNOTFOUND = "SubjectNotFound"
    UNKNOWNERROR = "UnknownError"

    def __str__(self) -> str:
        return str(self.value)
