from enum import Enum


class RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponseReportGenerationStatus(str, Enum):
    INPROGRESS = "inProgress"
    READY = "ready"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
