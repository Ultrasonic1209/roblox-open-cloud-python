from enum import Enum


class RobloxGameInternationalizationApiTranslationCountTranslatorType(str, Enum):
    AUTOMATION = "Automation"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
