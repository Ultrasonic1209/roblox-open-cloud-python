from enum import StrEnum


class BillingAccountSupportedPaymentTypesItem(StrEnum):
    ADS_CREDIT = "ADS_CREDIT"
    CREDIT_CARD = "CREDIT_CARD"
    INVOICE = "INVOICE"

    def __str__(self) -> str:
        return str(self.value)
