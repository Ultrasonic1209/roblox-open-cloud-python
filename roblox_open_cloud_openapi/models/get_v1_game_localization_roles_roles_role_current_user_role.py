from enum import Enum


class GetV1GameLocalizationRolesRolesRoleCurrentUserRole(str, Enum):
    TRANSLATOR = "translator"

    def __str__(self) -> str:
        return str(self.value)
