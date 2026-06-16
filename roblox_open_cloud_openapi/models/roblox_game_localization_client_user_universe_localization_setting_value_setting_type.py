from enum import Enum


class RobloxGameLocalizationClientUserUniverseLocalizationSettingValueSettingType(str, Enum):
    LANGUAGEFAMILY = "LanguageFamily"
    SOURCEORTRANSLATION = "SourceOrTranslation"
    SUPPORTEDLOCALE = "SupportedLocale"

    def __str__(self) -> str:
        return str(self.value)
