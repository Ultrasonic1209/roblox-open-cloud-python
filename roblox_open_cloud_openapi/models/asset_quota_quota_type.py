from enum import Enum


class AssetQuotaQuotaType(str, Enum):
    QUOTA_TYPE_UNSPECIFIED = "QUOTA_TYPE_UNSPECIFIED"
    RATE_LIMIT_CREATOR_STORE_DISTRIBUTE = "RATE_LIMIT_CREATOR_STORE_DISTRIBUTE"
    RATE_LIMIT_UPLOAD = "RATE_LIMIT_UPLOAD"

    def __str__(self) -> str:
        return str(self.value)
