from enum import StrEnum


class DataStoreEntryState(StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
