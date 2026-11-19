from enum import StrEnum


class ListPaymentActivitiesLedger(StrEnum):
    AD_CREDIT = "AD_CREDIT"
    CARD = "CARD"

    def __str__(self) -> str:
        return str(self.value)
