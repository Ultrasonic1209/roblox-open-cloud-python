from enum import StrEnum


class GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType(StrEnum):
    LANGUAGE = "Language"
    LOCALE = "Locale"

    def __str__(self) -> str:
        return str(self.value)
