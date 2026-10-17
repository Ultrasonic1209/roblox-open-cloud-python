from enum import StrEnum


class RobloxGameInternationalizationApiTranslationCountGameInfoResponseStatus(StrEnum):
    GAMEDOESNOTEXIST = "GameDoesNotExist"
    GAMEDOESNOTHAVETABLE = "GameDoesNotHaveTable"
    INSUFFICIENTPERMISSION = "InsufficientPermission"
    LANGUAGEORLOCALEISSOURCE = "LanguageOrLocaleIsSource"
    LANGUAGEORLOCALENOTSUPPORTEDFORGAME = "LanguageOrLocaleNotSupportedForGame"
    LANGUAGEORLOCALESUPPORTEDFORGAME = "LanguageOrLocaleSupportedForGame"
    UNKNOWNERROR = "UnknownError"

    def __str__(self) -> str:
        return str(self.value)
