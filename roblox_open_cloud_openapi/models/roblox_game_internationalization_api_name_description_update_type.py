from enum import Enum


class RobloxGameInternationalizationApiNameDescriptionUpdateType(str, Enum):
    DESCRIPTION = "Description"
    INVALID = "Invalid"
    NAME = "Name"

    def __str__(self) -> str:
        return str(self.value)
