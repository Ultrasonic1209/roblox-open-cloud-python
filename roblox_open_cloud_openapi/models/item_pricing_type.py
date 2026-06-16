from enum import Enum


class ItemPricingType(str, Enum):
    ALL = "All"
    PAIDANDLIMITED = "PaidAndLimited"
    UNDEFINED = "Undefined"

    def __str__(self) -> str:
        return str(self.value)
