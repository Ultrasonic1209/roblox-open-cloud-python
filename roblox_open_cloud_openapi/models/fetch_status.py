from enum import Enum


class FetchStatus(str, Enum):
    FAILURE = "Failure"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
