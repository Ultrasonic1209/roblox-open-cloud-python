from enum import StrEnum


class OrganizationsServiceApiSortOrder(StrEnum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
