from enum import IntEnum


class PlaceContentPreference(IntEnum):
    NONE = 0
    ALL = 1
    MENTIONS_AND_REPLIES = 2
    UNKNOWN = 3

    def __str__(self) -> str:
        return str(self.value)
