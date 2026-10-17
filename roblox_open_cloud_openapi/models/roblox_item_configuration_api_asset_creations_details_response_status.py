from enum import StrEnum


class RobloxItemConfigurationApiAssetCreationsDetailsResponseStatus(StrEnum):
    DELAYEDRELEASE = "DelayedRelease"
    FREE = "Free"
    MODERATED = "Moderated"
    OFFSALE = "OffSale"
    ONSALE = "OnSale"
    REVIEWAPPROVED = "ReviewApproved"
    REVIEWPENDING = "ReviewPending"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
