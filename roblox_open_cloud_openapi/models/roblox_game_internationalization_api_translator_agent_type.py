from enum import Enum


class RobloxGameInternationalizationApiTranslatorAgentType(str, Enum):
    AUTOMATION = "Automation"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
