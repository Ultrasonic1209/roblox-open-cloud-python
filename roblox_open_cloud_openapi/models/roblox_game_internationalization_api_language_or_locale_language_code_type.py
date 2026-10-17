from enum import StrEnum


class RobloxGameInternationalizationApiLanguageOrLocaleLanguageCodeType(StrEnum):
    LANGUAGE = "Language"
    LOCALE = "Locale"

    def __str__(self) -> str:
        return str(self.value)
