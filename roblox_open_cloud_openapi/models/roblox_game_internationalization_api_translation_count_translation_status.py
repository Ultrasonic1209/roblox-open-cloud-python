from enum import Enum


class RobloxGameInternationalizationApiTranslationCountTranslationStatus(str, Enum):
    APPROVED = "Approved"

    def __str__(self) -> str:
        return str(self.value)
