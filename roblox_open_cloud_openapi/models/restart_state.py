from enum import Enum


class RestartState(str, Enum):
    DELAYING = "DELAYING"
    RESTARTING = "RESTARTING"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
