from enum import Enum


class RobloxGroupsApiSetFeaturesRequestModelFeaturesForumRead(str, Enum):
    BLOCKED = "Blocked"
    ON = "On"

    def __str__(self) -> str:
        return str(self.value)
