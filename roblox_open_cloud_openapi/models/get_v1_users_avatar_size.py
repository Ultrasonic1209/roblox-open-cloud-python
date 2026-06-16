from enum import Enum


class GetV1UsersAvatarSize(str, Enum):
    VALUE_0 = "30x30"
    VALUE_1 = "48x48"
    VALUE_10 = "250x250"
    VALUE_11 = "352x352"
    VALUE_12 = "420x420"
    VALUE_13 = "720x720"
    VALUE_2 = "60x60"
    VALUE_3 = "75x75"
    VALUE_4 = "100x100"
    VALUE_5 = "110x110"
    VALUE_6 = "140x140"
    VALUE_7 = "150x150"
    VALUE_8 = "150x200"
    VALUE_9 = "180x180"

    def __str__(self) -> str:
        return str(self.value)
