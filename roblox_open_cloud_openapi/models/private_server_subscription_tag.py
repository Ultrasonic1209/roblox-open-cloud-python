from enum import StrEnum


class PrivateServerSubscriptionTag(StrEnum):
    INVALID = "Invalid"
    ROBLOXSUBSCRIPTION = "RobloxSubscription"
    ROBLOXSUBSCRIPTIONACTIVEBENEFIT = "RobloxSubscriptionActiveBenefit"

    def __str__(self) -> str:
        return str(self.value)
