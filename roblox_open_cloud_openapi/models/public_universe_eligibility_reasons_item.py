from enum import StrEnum


class PublicUniverseEligibilityReasonsItem(StrEnum):
    BLOCKED = "BLOCKED"
    NO_PERMISSION = "NO_PERMISSION"
    OBJECTIVE_NOT_SUPPORTED = "OBJECTIVE_NOT_SUPPORTED"

    def __str__(self) -> str:
        return str(self.value)
