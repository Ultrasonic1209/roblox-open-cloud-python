from enum import StrEnum


class GroupsApiRobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorTypeType(StrEnum):
    EXPERIENCE = "Experience"
    GROUP = "Group"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
