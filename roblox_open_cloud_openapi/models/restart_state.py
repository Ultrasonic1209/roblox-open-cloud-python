from enum import StrEnum


class RestartState(StrEnum):
    DELAYING = "DELAYING"
    RESTARTING = "RESTARTING"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
