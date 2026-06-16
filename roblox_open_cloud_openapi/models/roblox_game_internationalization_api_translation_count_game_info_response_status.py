from enum import Enum


class RobloxGameInternationalizationApiTranslationCountGameInfoResponseStatus(str, Enum):
    GAMEDOESNOTEXIST = "GameDoesNotExist"
    GAMEDOESNOTHAVETABLE = "GameDoesNotHaveTable"
    INSUFFICIENTPERMISSION = "InsufficientPermission"
    LANGUAGEORLOCALEISSOURCE = "LanguageOrLocaleIsSource"
    LANGUAGEORLOCALENOTSUPPORTEDFORGAME = "LanguageOrLocaleNotSupportedForGame"
    LANGUAGEORLOCALESUPPORTEDFORGAME = "LanguageOrLocaleSupportedForGame"
    UNKNOWNERROR = "UnknownError"

    def __str__(self) -> str:
        return str(self.value)
