from enum import Enum


class RobloxLocalizationtablesLocalizationtablesV1ChangeAgentChangeAgentType(str, Enum):
    AUTOMATION = "Automation"
    DEFAULT = "Default"
    INVALID = "Invalid"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
