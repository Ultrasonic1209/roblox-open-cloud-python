from enum import StrEnum


class RobloxGroupsApiGroupSettingsResponseVerificationLevel(StrEnum):
    HIGH = "High"
    LOW = "Low"
    MEDIUM = "Medium"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
