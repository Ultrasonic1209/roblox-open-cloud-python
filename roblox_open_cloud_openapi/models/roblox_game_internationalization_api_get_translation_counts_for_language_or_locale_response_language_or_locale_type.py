from enum import Enum


class RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponseLanguageOrLocaleType(str, Enum):
    LANGUAGE = "Language"
    LOCALE = "Locale"

    def __str__(self) -> str:
        return str(self.value)
