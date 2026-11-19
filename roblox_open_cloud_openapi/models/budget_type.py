from enum import StrEnum


class BudgetType(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"

    def __str__(self) -> str:
        return str(self.value)
