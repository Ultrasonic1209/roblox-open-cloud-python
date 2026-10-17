from enum import StrEnum


class RobloxLocalizationTablesApiEntryTranslationFeedbackReasonsItem(StrEnum):
    INACCURATE = "Inaccurate"
    INAPPROPRIATE = "Inappropriate"
    NONE = "None"
    SPELLINGORGRAMMAR = "SpellingOrGrammar"
    UNTRANSLATED = "Untranslated"

    def __str__(self) -> str:
        return str(self.value)
