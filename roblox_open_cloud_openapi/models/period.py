from enum import StrEnum


class Period(StrEnum):
    DAY = "DAY"
    MONTH = "MONTH"
    UNSPECIFIED = "UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
