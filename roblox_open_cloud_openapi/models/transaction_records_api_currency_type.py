from enum import Enum


class TransactionRecordsApiCurrencyType(str, Enum):
    ROBUX = "Robux"
    TICKETS = "Tickets"

    def __str__(self) -> str:
        return str(self.value)
