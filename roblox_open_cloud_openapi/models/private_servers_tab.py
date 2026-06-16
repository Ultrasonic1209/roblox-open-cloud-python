from enum import Enum


class PrivateServersTab(str, Enum):
    MYPRIVATESERVERS = "MyPrivateServers"
    OTHERPRIVATESERVERS = "OtherPrivateServers"

    def __str__(self) -> str:
        return str(self.value)
