from enum import StrEnum


class PaymentMethodType(StrEnum):
    CARD = "CARD"
    INVOICE = "INVOICE"

    def __str__(self) -> str:
        return str(self.value)
