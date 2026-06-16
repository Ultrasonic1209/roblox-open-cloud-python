from enum import Enum


class RobloxLocalizationTablesApiEntryTranslationFeedbackReasonsItem(str, Enum):
    INACCURATE = "Inaccurate"
    INAPPROPRIATE = "Inappropriate"
    NONE = "None"
    SPELLINGORGRAMMAR = "SpellingOrGrammar"
    UNTRANSLATED = "Untranslated"

    def __str__(self) -> str:
        return str(self.value)
