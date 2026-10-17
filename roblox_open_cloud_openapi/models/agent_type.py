from enum import StrEnum


class AgentType(StrEnum):
    GROUP = "Group"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
