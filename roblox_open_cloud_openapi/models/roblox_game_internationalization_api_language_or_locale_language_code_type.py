from enum import Enum


class RobloxGameInternationalizationApiLanguageOrLocaleLanguageCodeType(str, Enum):
    LANGUAGE = "Language"
    LOCALE = "Locale"

    def __str__(self) -> str:
        return str(self.value)
