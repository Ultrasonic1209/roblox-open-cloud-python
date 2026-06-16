from enum import Enum


class CloudGetMemoryStoreFlushOperationScope(str, Enum):
    LIVE = "LIVE"
    TEST = "TEST"

    def __str__(self) -> str:
        return str(self.value)
