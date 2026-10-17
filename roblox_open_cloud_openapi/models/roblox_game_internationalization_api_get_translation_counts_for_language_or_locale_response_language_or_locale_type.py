from enum import StrEnum


class RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponseLanguageOrLocaleType(StrEnum):
    LANGUAGE = "Language"
    LOCALE = "Locale"

    def __str__(self) -> str:
        return str(self.value)
