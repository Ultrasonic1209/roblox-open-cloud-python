from enum import Enum


class RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequestReportType(str, Enum):
    GAMETRANSLATIONSTATUS = "GameTranslationStatus"
    GAMETRANSLATIONSTATUSFORTRANSLATOR = "GameTranslationStatusForTranslator"
    GAMETRANSLATIONSTATUSFORTRANSLATORGROUP = "GameTranslationStatusForTranslatorGroup"
    TEST = "Test"

    def __str__(self) -> str:
        return str(self.value)
