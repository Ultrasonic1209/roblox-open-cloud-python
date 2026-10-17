from enum import StrEnum


class GetV2SearchItemsDetailsSortOrder(StrEnum):
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
