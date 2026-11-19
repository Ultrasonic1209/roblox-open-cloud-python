from enum import StrEnum


class BudgetConstraintBudgetType(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"

    def __str__(self) -> str:
        return str(self.value)
