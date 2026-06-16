from enum import Enum


class SubscriptionPaymentProvider(str, Enum):
    APPLE = "APPLE"
    GOOGLE = "GOOGLE"
    PAYMENT_PROVIDER_UNSPECIFIED = "PAYMENT_PROVIDER_UNSPECIFIED"
    ROBLOX_CREDIT = "ROBLOX_CREDIT"
    ROBUX = "ROBUX"
    STRIPE = "STRIPE"

    def __str__(self) -> str:
        return str(self.value)
