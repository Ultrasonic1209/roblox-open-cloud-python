from enum import StrEnum


class TransactionRecordsApiCurrencyType(StrEnum):
    ROBUX = "Robux"
    TICKETS = "Tickets"

    def __str__(self) -> str:
        return str(self.value)
