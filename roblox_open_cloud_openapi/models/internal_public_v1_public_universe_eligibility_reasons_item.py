from enum import StrEnum


class InternalPublicV1PublicUniverseEligibilityReasonsItem(StrEnum):
    BLOCKED = "BLOCKED"
    NO_PERMISSION = "NO_PERMISSION"

    def __str__(self) -> str:
        return str(self.value)
