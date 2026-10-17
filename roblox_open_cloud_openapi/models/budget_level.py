from enum import Enum


class BudgetLevel(str, Enum):
    RESOURCEONLY = "ResourceOnly"
    SERVICEONLY = "ServiceOnly"

    def __str__(self) -> str:
        return str(self.value)
