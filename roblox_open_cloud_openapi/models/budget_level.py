from enum import StrEnum


class BudgetLevel(StrEnum):
    RESOURCEONLY = "ResourceOnly"
    SERVICEONLY = "ServiceOnly"

    def __str__(self) -> str:
        return str(self.value)
