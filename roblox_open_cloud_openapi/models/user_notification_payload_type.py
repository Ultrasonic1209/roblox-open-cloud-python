from enum import StrEnum


class UserNotificationPayloadType(StrEnum):
    MOMENT = "MOMENT"
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
