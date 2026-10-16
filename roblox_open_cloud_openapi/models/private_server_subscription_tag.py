from enum import Enum


class PrivateServerSubscriptionTag(str, Enum):
    INVALID = "Invalid"
    ROBLOXSUBSCRIPTION = "RobloxSubscription"
    ROBLOXSUBSCRIPTIONACTIVEBENEFIT = "RobloxSubscriptionActiveBenefit"

    def __str__(self) -> str:
        return str(self.value)
