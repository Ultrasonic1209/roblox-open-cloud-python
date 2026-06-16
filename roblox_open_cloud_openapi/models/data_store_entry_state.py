from enum import Enum


class DataStoreEntryState(str, Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
