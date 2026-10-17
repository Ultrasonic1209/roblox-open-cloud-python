from enum import StrEnum


class GetV2UsersUserIdGamesSortOrder(StrEnum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
