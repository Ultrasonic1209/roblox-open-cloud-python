from enum import StrEnum


class AlertStorageAlertInterval(StrEnum):
    HALF_HOUR = "HalfHour"
    ONE_DAY = "OneDay"
    ONE_HOUR = "OneHour"
    ONE_MINUTE = "OneMinute"

    def __str__(self) -> str:
        return str(self.value)
