from enum import Enum


class GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder(str, Enum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
