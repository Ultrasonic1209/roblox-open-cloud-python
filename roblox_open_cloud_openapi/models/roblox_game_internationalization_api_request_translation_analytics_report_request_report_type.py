from enum import StrEnum


class RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequestReportType(StrEnum):
    GAMETRANSLATIONSTATUS = "GameTranslationStatus"
    GAMETRANSLATIONSTATUSFORTRANSLATOR = "GameTranslationStatusForTranslator"
    GAMETRANSLATIONSTATUSFORTRANSLATORGROUP = "GameTranslationStatusForTranslatorGroup"
    TEST = "Test"

    def __str__(self) -> str:
        return str(self.value)
