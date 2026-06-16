from enum import Enum


class TransactionRecordsApiSortOrder(str, Enum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
