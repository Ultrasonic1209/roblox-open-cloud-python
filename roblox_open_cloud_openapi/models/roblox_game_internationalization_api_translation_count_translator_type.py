from enum import StrEnum


class RobloxGameInternationalizationApiTranslationCountTranslatorType(StrEnum):
    AUTOMATION = "Automation"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
