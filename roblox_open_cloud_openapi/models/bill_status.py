from enum import StrEnum


class BillStatus(StrEnum):
    CLOSED = "Closed"
    INVALID = "Invalid"
    PAID = "Paid"
    UNPAID = "Unpaid"

    def __str__(self) -> str:
        return str(self.value)
