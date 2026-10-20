from enum import StrEnum


class InternalPublicV1BidStrategy(StrEnum):
    AUTOMATED = "AUTOMATED"

    def __str__(self) -> str:
        return str(self.value)
