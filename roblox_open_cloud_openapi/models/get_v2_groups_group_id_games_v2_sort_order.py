from enum import StrEnum


class GetV2GroupsGroupIdGamesV2SortOrder(StrEnum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
