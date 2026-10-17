from enum import StrEnum


class HttpVersionPolicy(StrEnum):
    REQUESTVERSIONEXACT = "RequestVersionExact"
    REQUESTVERSIONORHIGHER = "RequestVersionOrHigher"
    REQUESTVERSIONORLOWER = "RequestVersionOrLower"

    def __str__(self) -> str:
        return str(self.value)
