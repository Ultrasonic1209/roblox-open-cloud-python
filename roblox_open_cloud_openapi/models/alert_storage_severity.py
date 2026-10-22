from enum import StrEnum


class AlertStorageSeverity(StrEnum):
    SEV_0 = "SEV_0"
    SEV_1 = "SEV_1"
    SEV_2 = "SEV_2"

    def __str__(self) -> str:
        return str(self.value)
