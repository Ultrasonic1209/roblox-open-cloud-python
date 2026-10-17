from enum import StrEnum


class RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestSortOrder(StrEnum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
