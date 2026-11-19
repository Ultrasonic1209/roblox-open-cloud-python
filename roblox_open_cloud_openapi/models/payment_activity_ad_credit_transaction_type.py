from enum import StrEnum


class PaymentActivityAdCreditTransactionType(StrEnum):
    ADJUSTMENT = "ADJUSTMENT"
    AUTO_DEPOSIT = "AUTO_DEPOSIT"
    DEBIT = "DEBIT"
    DEPOSIT = "DEPOSIT"
    PROMOTION = "PROMOTION"
    REFUND = "REFUND"

    def __str__(self) -> str:
        return str(self.value)
