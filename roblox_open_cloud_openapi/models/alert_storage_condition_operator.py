from enum import Enum


class AlertStorageConditionOperator(str, Enum):
    GT = "Gt"
    GTE = "Gte"
    LT = "Lt"
    LTE = "Lte"

    def __str__(self) -> str:
        return str(self.value)
