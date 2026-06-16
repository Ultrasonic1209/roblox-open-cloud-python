from enum import Enum


class SubjectType(str, Enum):
    ALL = "All"
    GROUP = "Group"
    GROUPROLESET = "GroupRoleset"
    INVALID = "Invalid"
    UNIVERSE = "Universe"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
