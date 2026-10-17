from enum import StrEnum


class RobloxTranslationRolesApiAssigneeType(StrEnum):
    GROUP = "group"
    GROUPROLE = "groupRole"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
