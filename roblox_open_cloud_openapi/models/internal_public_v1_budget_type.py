from enum import StrEnum


class InternalPublicV1BudgetType(StrEnum):
    DAILY = "DAILY"
    LIFETIME = "LIFETIME"

    def __str__(self) -> str:
        return str(self.value)
