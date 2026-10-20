from enum import StrEnum


class InternalPublicV1BillingAccountType(StrEnum):
    INTERNAL = "INTERNAL"
    MANAGED = "MANAGED"
    SELF_SERVICE = "SELF_SERVICE"

    def __str__(self) -> str:
        return str(self.value)
