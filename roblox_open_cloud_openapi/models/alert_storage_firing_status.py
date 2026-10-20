from enum import StrEnum


class AlertStorageFiringStatus(StrEnum):
    FIRING = "Firing"
    OK = "OK"

    def __str__(self) -> str:
        return str(self.value)
