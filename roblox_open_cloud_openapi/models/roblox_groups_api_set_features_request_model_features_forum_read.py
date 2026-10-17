from enum import StrEnum


class RobloxGroupsApiSetFeaturesRequestModelFeaturesForumRead(StrEnum):
    BLOCKED = "Blocked"
    ON = "On"

    def __str__(self) -> str:
        return str(self.value)
