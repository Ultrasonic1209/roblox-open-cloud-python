from enum import Enum


class RobloxTranslationRolesApiUpdateRoleRequestRole(str, Enum):
    TRANSLATOR = "translator"

    def __str__(self) -> str:
        return str(self.value)
