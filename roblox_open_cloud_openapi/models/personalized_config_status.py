from enum import StrEnum


class PersonalizedConfigStatus(StrEnum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def __str__(self) -> str:
        return str(self.value)
