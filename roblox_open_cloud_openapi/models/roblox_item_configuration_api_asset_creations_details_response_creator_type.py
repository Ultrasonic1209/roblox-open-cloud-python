from enum import Enum


class RobloxItemConfigurationApiAssetCreationsDetailsResponseCreatorType(str, Enum):
    GROUP = "Group"
    UNKNOWN = "Unknown"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
