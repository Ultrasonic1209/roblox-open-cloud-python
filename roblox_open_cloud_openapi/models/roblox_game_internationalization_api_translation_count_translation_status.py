from enum import StrEnum


class RobloxGameInternationalizationApiTranslationCountTranslationStatus(StrEnum):
    APPROVED = "Approved"

    def __str__(self) -> str:
        return str(self.value)
