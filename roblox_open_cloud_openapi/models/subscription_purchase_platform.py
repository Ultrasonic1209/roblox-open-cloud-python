from enum import StrEnum


class SubscriptionPurchasePlatform(StrEnum):
    DESKTOP = "DESKTOP"
    MOBILE = "MOBILE"
    PURCHASE_PLATFORM_UNSPECIFIED = "PURCHASE_PLATFORM_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
