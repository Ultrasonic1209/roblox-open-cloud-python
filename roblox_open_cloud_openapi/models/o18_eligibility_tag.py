from enum import Enum


class O18EligibilityTag(str, Enum):
    NONE = "None"
    O18ELIGIBLE = "O18Eligible"
    O18ELIGIBLEANDPLUS = "O18EligibleAndPlus"

    def __str__(self) -> str:
        return str(self.value)
