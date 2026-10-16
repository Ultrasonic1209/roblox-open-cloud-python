from enum import Enum


class GetV2GroupsGroupIdGamesSortOrder(str, Enum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
