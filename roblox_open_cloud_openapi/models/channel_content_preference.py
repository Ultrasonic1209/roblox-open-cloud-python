from enum import IntEnum


class ChannelContentPreference(IntEnum):
    NONE = 0
    ALL = 1
    UNKNOWN = 2

    def __str__(self) -> str:
        return str(self.value)
