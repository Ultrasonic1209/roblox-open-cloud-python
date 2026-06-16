from enum import Enum


class GetV1GamesMultigetThumbnailsSize(str, Enum):
    VALUE_0 = "768x432"
    VALUE_1 = "576x324"
    VALUE_2 = "480x270"
    VALUE_3 = "384x216"
    VALUE_4 = "256x144"

    def __str__(self) -> str:
        return str(self.value)
