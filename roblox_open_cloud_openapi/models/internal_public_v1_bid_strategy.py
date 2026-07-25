from enum import Enum


class InternalPublicV1BidStrategy(str, Enum):
    AUTOMATED = "AUTOMATED"

    def __str__(self) -> str:
        return str(self.value)
