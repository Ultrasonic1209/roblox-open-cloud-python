from enum import StrEnum


class RobloxGameInternationalizationApiLanguageOrLocaleSettingsLanguageCodeType(StrEnum):
    LANGUAGE = "Language"
    LOCALE = "Locale"

    def __str__(self) -> str:
        return str(self.value)
