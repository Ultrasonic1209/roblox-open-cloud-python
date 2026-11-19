from enum import StrEnum


class QuotaType(StrEnum):
    RATE_LIMIT_CREATOR_STORE_DISTRIBUTE = "RATE_LIMIT_CREATOR_STORE_DISTRIBUTE"
    RATE_LIMIT_UPLOAD = "RATE_LIMIT_UPLOAD"
    UNSPECIFIED = "UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
