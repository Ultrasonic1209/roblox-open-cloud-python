from enum import Enum


class RsvpStatus(str, Enum):
    GOING = "going"
    MAYBEGOING = "maybeGoing"
    NONE = "none"
    NOTGOING = "notGoing"

    def __str__(self) -> str:
        return str(self.value)
