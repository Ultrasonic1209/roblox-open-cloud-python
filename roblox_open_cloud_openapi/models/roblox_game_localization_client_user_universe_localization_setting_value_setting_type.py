from enum import StrEnum


class RobloxGameLocalizationClientUserUniverseLocalizationSettingValueSettingType(StrEnum):
    LANGUAGEFAMILY = "LanguageFamily"
    SOURCEORTRANSLATION = "SourceOrTranslation"
    SUPPORTEDLOCALE = "SupportedLocale"

    def __str__(self) -> str:
        return str(self.value)
