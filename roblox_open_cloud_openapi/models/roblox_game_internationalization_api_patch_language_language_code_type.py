from enum import StrEnum


class RobloxGameInternationalizationApiPatchLanguageLanguageCodeType(StrEnum):
    LANGUAGE = "Language"
    LOCALE = "Locale"

    def __str__(self) -> str:
        return str(self.value)
