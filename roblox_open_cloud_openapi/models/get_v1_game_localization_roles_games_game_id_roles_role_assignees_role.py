from enum import StrEnum


class GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole(StrEnum):
    TRANSLATOR = "translator"

    def __str__(self) -> str:
        return str(self.value)
