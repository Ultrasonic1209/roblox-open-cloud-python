from enum import Enum


class GetV1AssetsthumbnailsRobloxComSize(str, Enum):
    VALUE_0 = "30x30"
    VALUE_1 = "42x42"
    VALUE_10 = "250x250"
    VALUE_11 = "256x144"
    VALUE_12 = "300x250"
    VALUE_13 = "304x166"
    VALUE_14 = "384x216"
    VALUE_15 = "396x216"
    VALUE_16 = "420x420"
    VALUE_17 = "480x270"
    VALUE_18 = "512x512"
    VALUE_19 = "576x324"
    VALUE_2 = "50x50"
    VALUE_20 = "700x700"
    VALUE_21 = "728x90"
    VALUE_22 = "768x432"
    VALUE_23 = "1200x80"
    VALUE_24 = "330x110"
    VALUE_25 = "660x220"
    VALUE_26 = "1320x440"
    VALUE_27 = "720x228"
    VALUE_28 = "1440x456"
    VALUE_29 = "930x480"
    VALUE_3 = "60x62"
    VALUE_4 = "75x75"
    VALUE_5 = "110x110"
    VALUE_6 = "140x140"
    VALUE_7 = "150x150"
    VALUE_8 = "160x100"
    VALUE_9 = "160x600"

    def __str__(self) -> str:
        return str(self.value)
