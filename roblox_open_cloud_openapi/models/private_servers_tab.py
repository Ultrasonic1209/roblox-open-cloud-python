from enum import StrEnum


class PrivateServersTab(StrEnum):
    MYPRIVATESERVERS = "MyPrivateServers"
    OTHERPRIVATESERVERS = "OtherPrivateServers"

    def __str__(self) -> str:
        return str(self.value)
