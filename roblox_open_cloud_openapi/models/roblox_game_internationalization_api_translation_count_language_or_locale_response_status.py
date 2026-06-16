from enum import Enum


class RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseStatus(str, Enum):
    LANGUAGEORLOCALENOTSUPPORTEDFORGAME = "LanguageOrLocaleNotSupportedForGame"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
