from enum import StrEnum


class RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseLanguageCodeType(StrEnum):
    LANGUAGE = "Language"
    LOCALE = "Locale"

    def __str__(self) -> str:
        return str(self.value)
