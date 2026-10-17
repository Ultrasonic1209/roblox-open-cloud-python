from enum import StrEnum


class RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseStatus(StrEnum):
    LANGUAGEORLOCALENOTSUPPORTEDFORGAME = "LanguageOrLocaleNotSupportedForGame"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
