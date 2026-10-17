from enum import StrEnum


class DataStoreState(StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
