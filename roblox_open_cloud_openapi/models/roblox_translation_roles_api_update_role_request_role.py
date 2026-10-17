from enum import StrEnum


class RobloxTranslationRolesApiUpdateRoleRequestRole(StrEnum):
    TRANSLATOR = "translator"

    def __str__(self) -> str:
        return str(self.value)
