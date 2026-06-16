from enum import Enum


class RobloxGameInternationalizationApiGetNameDescriptionHistoryV2RequestSortOrder(str, Enum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
