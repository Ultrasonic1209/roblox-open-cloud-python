from enum import StrEnum


class RobloxGameInternationalizationApiTranslatorAgentType(StrEnum):
    AUTOMATION = "Automation"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
