from enum import StrEnum


class GetV1BadgesIconsSize(StrEnum):
    VALUE_0 = "150x150"

    def __str__(self) -> str:
        return str(self.value)
