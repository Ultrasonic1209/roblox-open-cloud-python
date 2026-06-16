from enum import Enum


class GetV1UsersUserIdBadgesSortOrder(str, Enum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
