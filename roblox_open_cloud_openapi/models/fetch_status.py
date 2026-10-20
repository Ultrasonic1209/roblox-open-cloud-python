from enum import StrEnum


class FetchStatus(StrEnum):
    FAILURE = "Failure"
    SUCCESS = "Success"

    def __str__(self) -> str:
        return str(self.value)
