from enum import Enum


class CloudFlushMemoryStoreScope(str, Enum):
    LIVE = "LIVE"
    TEST = "TEST"

    def __str__(self) -> str:
        return str(self.value)
