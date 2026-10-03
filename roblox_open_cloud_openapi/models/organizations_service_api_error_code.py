from enum import Enum


class OrganizationsServiceApiErrorCode(str, Enum):
    FEATURENOTENABLED = "FeatureNotEnabled"
    FEATURENOTSUPPORTEDFORROLE = "FeatureNotSupportedForRole"
    GROUPFEATUREFROZEN = "GroupFeatureFrozen"
    GROUPMIGRATED = "GroupMigrated"
    INSUFFICIENTGROUPPERMISSION = "InsufficientGroupPermission"
    INSUFFICIENTPERMISSION = "InsufficientPermission"
    INTERNALERROR = "InternalError"
    INVALIDGROUPID = "InvalidGroupId"
    INVALIDINVITATIONSTATUS = "InvalidInvitationStatus"
    INVALIDPAGELIMIT = "InvalidPageLimit"
    INVALIDREQUESTBODY = "InvalidRequestBody"
    INVALIDSORTORDER = "InvalidSortOrder"
    INVALIDUNIVERSEID = "InvalidUniverseId"
    INVITATIONNOTFOUND = "InvitationNotFound"
    NEEDSSECUREENDPOINT = "NeedsSecureEndpoint"
    PERMISSIONNOTSUPPORTED = "PermissionNotSupported"
    ROLEIDMIGRATIONINPROGRESS = "RoleIdMigrationInProgress"
    ROLENAMERESERVED = "RoleNameReserved"
    ROLENOTFOUND = "RoleNotFound"
    TOOMANYREQUESTS = "TooManyRequests"
    TOOMANYROLES = "TooManyRoles"
    TOOMANYUSERS = "TooManyUsers"
    UNIFICATIONINPROGRESS = "UnificationInProgress"
    USERINMAXGROUPS = "UserInMaxGroups"
    USERNOTINGROUP = "UserNotInGroup"

    def __str__(self) -> str:
        return str(self.value)
