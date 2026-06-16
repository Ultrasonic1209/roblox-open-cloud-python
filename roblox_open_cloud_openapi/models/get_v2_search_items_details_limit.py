from enum import IntEnum


class GetV2SearchItemsDetailsLimit(IntEnum):
    VALUE_10 = 10
    VALUE_28 = 28
    VALUE_30 = 30
    VALUE_60 = 60
    VALUE_120 = 120

    def __str__(self) -> str:
        return str(self.value)
