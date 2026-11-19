from enum import StrEnum


class BillingAccountOptionStatus(StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DISABLED = "DISABLED"

    def __str__(self) -> str:
        return str(self.value)
