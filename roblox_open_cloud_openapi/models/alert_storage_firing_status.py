from enum import Enum


class AlertStorageFiringStatus(str, Enum):
    FIRING = "Firing"
    OK = "OK"

    def __str__(self) -> str:
        return str(self.value)
