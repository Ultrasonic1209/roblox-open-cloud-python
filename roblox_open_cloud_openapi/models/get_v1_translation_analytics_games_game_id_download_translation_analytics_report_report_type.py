from enum import Enum


class GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType(str, Enum):
    GAMETRANSLATIONSTATUS = "GameTranslationStatus"
    GAMETRANSLATIONSTATUSFORTRANSLATOR = "GameTranslationStatusForTranslator"
    GAMETRANSLATIONSTATUSFORTRANSLATORGROUP = "GameTranslationStatusForTranslatorGroup"
    TEST = "Test"

    def __str__(self) -> str:
        return str(self.value)
