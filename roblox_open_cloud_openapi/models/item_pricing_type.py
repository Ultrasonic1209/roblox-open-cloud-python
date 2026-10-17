from enum import StrEnum


class ItemPricingType(StrEnum):
    ALL = "All"
    PAIDANDLIMITED = "PaidAndLimited"
    UNDEFINED = "Undefined"

    def __str__(self) -> str:
        return str(self.value)
