from enum import Enum


class UserNotificationPayloadType(str, Enum):
    MOMENT = "MOMENT"
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
