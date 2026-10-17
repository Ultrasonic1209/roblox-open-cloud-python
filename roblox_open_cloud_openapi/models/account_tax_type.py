from enum import Enum


class AccountTaxType(str, Enum):
    BUSINESS = "Business"
    INDIVIDUAL = "Individual"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
