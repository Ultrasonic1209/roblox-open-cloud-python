from enum import Enum


class EventNotificationAudience(str, Enum):
    ALL = "all"
    GROUP = "group"
    NONE = "none"
    RSVP = "rsvp"
    SUBSCRIBED = "subscribed"

    def __str__(self) -> str:
        return str(self.value)
