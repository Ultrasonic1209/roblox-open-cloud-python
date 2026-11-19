from enum import StrEnum


class RobloxSubscriptionsOpenCloudV2SubscriptionPaymentProvider(StrEnum):
    APPLE = "APPLE"
    GOOGLE = "GOOGLE"
    PAYMENT_PROVIDER_UNSPECIFIED = "PAYMENT_PROVIDER_UNSPECIFIED"
    ROBLOX_CREDIT = "ROBLOX_CREDIT"
    ROBUX = "ROBUX"
    STRIPE = "STRIPE"

    def __str__(self) -> str:
        return str(self.value)
