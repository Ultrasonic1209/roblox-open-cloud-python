from enum import Enum


class AlertStorageAlertInterval(str, Enum):
    HALF_HOUR = "HalfHour"
    ONE_DAY = "OneDay"
    ONE_HOUR = "OneHour"
    ONE_MINUTE = "OneMinute"

    def __str__(self) -> str:
        return str(self.value)
