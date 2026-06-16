from enum import Enum


class GetV2SearchItemsDetailsSortOrder(str, Enum):
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
