from enum import StrEnum


class GetV1GroupsGroupIdBansSortOrder(StrEnum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
