from enum import StrEnum


class SummaryCardTileTitleSourceType0Type0(StrEnum):
    DASHBOARD_TITLE_SOURCE_AUTO = "DASHBOARD_TITLE_SOURCE_AUTO"
    DASHBOARD_TITLE_SOURCE_CUSTOM = "DASHBOARD_TITLE_SOURCE_CUSTOM"
    DASHBOARD_TITLE_SOURCE_INVALID = "DASHBOARD_TITLE_SOURCE_INVALID"

    def __str__(self) -> str:
        return str(self.value)
