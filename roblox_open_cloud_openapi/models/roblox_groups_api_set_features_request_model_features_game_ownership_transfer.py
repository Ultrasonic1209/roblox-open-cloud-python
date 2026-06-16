from enum import Enum


class RobloxGroupsApiSetFeaturesRequestModelFeaturesGameOwnershipTransfer(str, Enum):
    BLOCKED = "Blocked"
    ON = "On"

    def __str__(self) -> str:
        return str(self.value)
