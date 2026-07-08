from enum import Enum


class MetricGranularity(str, Enum):
    HALFHOUR = "HalfHour"
    NONE = "None"
    ONEDAY = "OneDay"
    ONEHOUR = "OneHour"
    ONEMINUTE = "OneMinute"
    ONEMONTH = "OneMonth"
    ONEWEEK = "OneWeek"

    def __str__(self) -> str:
        return str(self.value)
