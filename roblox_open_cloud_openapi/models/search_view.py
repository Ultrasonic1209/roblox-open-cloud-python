from enum import Enum


class SearchView(str, Enum):
    CORE = "Core"
    FULL = "Full"
    I_DS = "IDs"

    def __str__(self) -> str:
        return str(self.value)
