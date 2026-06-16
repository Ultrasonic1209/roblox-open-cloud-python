from enum import Enum


class GetV1BadgesIconsSize(str, Enum):
    VALUE_0 = "150x150"

    def __str__(self) -> str:
        return str(self.value)
