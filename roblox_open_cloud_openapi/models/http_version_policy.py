from enum import Enum


class HttpVersionPolicy(str, Enum):
    REQUESTVERSIONEXACT = "RequestVersionExact"
    REQUESTVERSIONORHIGHER = "RequestVersionOrHigher"
    REQUESTVERSIONORLOWER = "RequestVersionOrLower"

    def __str__(self) -> str:
        return str(self.value)
