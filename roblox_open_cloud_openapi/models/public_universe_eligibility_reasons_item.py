from enum import StrEnum


class PublicUniverseEligibilityReasonsItem(StrEnum):
    BLOCKED = "BLOCKED"
    NO_PERMISSION = "NO_PERMISSION"

    def __str__(self) -> str:
        return str(self.value)
