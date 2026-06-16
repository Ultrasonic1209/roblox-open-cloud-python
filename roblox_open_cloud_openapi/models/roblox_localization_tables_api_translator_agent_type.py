from enum import Enum


class RobloxLocalizationTablesApiTranslatorAgentType(str, Enum):
    AUTOMATION = "Automation"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
