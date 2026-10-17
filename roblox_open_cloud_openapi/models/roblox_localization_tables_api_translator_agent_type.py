from enum import StrEnum


class RobloxLocalizationTablesApiTranslatorAgentType(StrEnum):
    AUTOMATION = "Automation"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
