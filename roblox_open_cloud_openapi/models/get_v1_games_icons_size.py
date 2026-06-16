from enum import Enum


class GetV1GamesIconsSize(str, Enum):
    VALUE_0 = "50x50"
    VALUE_1 = "128x128"
    VALUE_2 = "150x150"
    VALUE_3 = "256x256"
    VALUE_4 = "420x420"
    VALUE_5 = "512x512"

    def __str__(self) -> str:
        return str(self.value)
