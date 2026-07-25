from enum import Enum


class InternalPublicV1BudgetType(str, Enum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"

    def __str__(self) -> str:
        return str(self.value)
