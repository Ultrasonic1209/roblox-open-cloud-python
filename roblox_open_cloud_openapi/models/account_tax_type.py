from enum import StrEnum


class AccountTaxType(StrEnum):
    BUSINESS = "Business"
    INDIVIDUAL = "Individual"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
