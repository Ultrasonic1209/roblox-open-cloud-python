from enum import StrEnum


class CloudGetMemoryStoreFlushOperationScope(StrEnum):
    LIVE = "LIVE"
    TEST = "TEST"

    def __str__(self) -> str:
        return str(self.value)
