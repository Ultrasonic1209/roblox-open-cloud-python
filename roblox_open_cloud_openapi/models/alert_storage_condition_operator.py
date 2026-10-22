from enum import StrEnum


class AlertStorageConditionOperator(StrEnum):
    GT = "Gt"
    GTE = "Gte"
    LT = "Lt"
    LTE = "Lte"

    def __str__(self) -> str:
        return str(self.value)
