from enum import Enum


class AlertStorageSeverity(str, Enum):
    SEV_0 = "SEV_0"
    SEV_1 = "SEV_1"
    SEV_2 = "SEV_2"

    def __str__(self) -> str:
        return str(self.value)
