from enum import Enum


class InternalPublicV1BillingAccountType(str, Enum):
    INTERNAL = "INTERNAL"
    MANAGED = "MANAGED"
    SELF_SERVICE = "SELF_SERVICE"

    def __str__(self) -> str:
        return str(self.value)
