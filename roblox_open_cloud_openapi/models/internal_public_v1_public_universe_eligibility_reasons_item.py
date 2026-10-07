from enum import Enum


class InternalPublicV1PublicUniverseEligibilityReasonsItem(str, Enum):
    BLOCKED = "BLOCKED"
    NO_PERMISSION = "NO_PERMISSION"

    def __str__(self) -> str:
        return str(self.value)
