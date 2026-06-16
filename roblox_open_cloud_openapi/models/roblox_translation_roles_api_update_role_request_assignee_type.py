from enum import Enum


class RobloxTranslationRolesApiUpdateRoleRequestAssigneeType(str, Enum):
    GROUP = "group"
    GROUPROLE = "groupRole"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
