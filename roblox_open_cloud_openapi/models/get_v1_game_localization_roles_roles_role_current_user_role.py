from enum import StrEnum


class GetV1GameLocalizationRolesRolesRoleCurrentUserRole(StrEnum):
    TRANSLATOR = "translator"

    def __str__(self) -> str:
        return str(self.value)
