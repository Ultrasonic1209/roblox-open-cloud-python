from enum import StrEnum


class RobloxGameInternationalizationApiNameDescriptionUpdateType(StrEnum):
    DESCRIPTION = "Description"
    INVALID = "Invalid"
    NAME = "Name"

    def __str__(self) -> str:
        return str(self.value)
