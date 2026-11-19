from enum import StrEnum


class ListPaymentActivitiesType(StrEnum):
    CHARGE = "CHARGE"
    REFUND = "REFUND"

    def __str__(self) -> str:
        return str(self.value)
