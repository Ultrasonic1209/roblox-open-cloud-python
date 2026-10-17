from enum import StrEnum


class RobloxItemConfigurationApiAssetCreationsDetailsResponseCreatorType(StrEnum):
    GROUP = "Group"
    UNKNOWN = "Unknown"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
