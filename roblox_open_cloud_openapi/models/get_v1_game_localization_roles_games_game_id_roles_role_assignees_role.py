from enum import Enum


class GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole(str, Enum):
    TRANSLATOR = "translator"

    def __str__(self) -> str:
        return str(self.value)
