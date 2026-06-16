from enum import Enum


class CloudGetSubscriptionView(str, Enum):
    BASIC = "BASIC"
    FULL = "FULL"
    VIEW_UNSPECIFIED = "VIEW_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
