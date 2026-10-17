from enum import StrEnum


class RobloxLocalizationtablesLocalizationtablesV1ChangeAgentChangeAgentType(StrEnum):
    AUTOMATION = "Automation"
    DEFAULT = "Default"
    INVALID = "Invalid"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
