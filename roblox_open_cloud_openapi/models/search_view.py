from enum import StrEnum


class SearchView(StrEnum):
    CORE = "Core"
    FULL = "Full"
    I_DS = "IDs"

    def __str__(self) -> str:
        return str(self.value)
