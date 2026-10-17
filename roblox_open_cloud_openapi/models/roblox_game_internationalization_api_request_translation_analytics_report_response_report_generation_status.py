from enum import StrEnum


class RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponseReportGenerationStatus(StrEnum):
    INPROGRESS = "inProgress"
    READY = "ready"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
