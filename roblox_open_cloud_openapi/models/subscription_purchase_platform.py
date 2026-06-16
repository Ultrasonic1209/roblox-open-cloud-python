from enum import Enum


class SubscriptionPurchasePlatform(str, Enum):
    DESKTOP = "DESKTOP"
    MOBILE = "MOBILE"
    PURCHASE_PLATFORM_UNSPECIFIED = "PURCHASE_PLATFORM_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
