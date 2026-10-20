from enum import StrEnum


class RsvpStatus(StrEnum):
    GOING = "going"
    MAYBEGOING = "maybeGoing"
    NONE = "none"
    NOTGOING = "notGoing"

    def __str__(self) -> str:
        return str(self.value)
