from enum import StrEnum


class GetV1UsersTargetUserIdFollowingsSortOrder(StrEnum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
