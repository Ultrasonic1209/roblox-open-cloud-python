from enum import Enum


class BillStatus(str, Enum):
    CLOSED = "Closed"
    INVALID = "Invalid"
    PAID = "Paid"
    UNPAID = "Unpaid"

    def __str__(self) -> str:
        return str(self.value)
