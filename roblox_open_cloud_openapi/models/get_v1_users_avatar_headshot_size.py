from enum import Enum


class GetV1UsersAvatarHeadshotSize(str, Enum):
    VALUE_0 = "48x48"
    VALUE_1 = "50x50"
    VALUE_10 = "720x720"
    VALUE_2 = "60x60"
    VALUE_3 = "75x75"
    VALUE_4 = "100x100"
    VALUE_5 = "110x110"
    VALUE_6 = "150x150"
    VALUE_7 = "180x180"
    VALUE_8 = "352x352"
    VALUE_9 = "420x420"

    def __str__(self) -> str:
        return str(self.value)
