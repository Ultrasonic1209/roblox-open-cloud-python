from enum import Enum


class ServerStatus(str, Enum):
    ACTIVE = "active"
    CRASHED = "crashed"
    MODERATED = "moderated"
    OUT_OF_MEMORY = "out_of_memory"
    PENDING = "pending"
    RESTARTED = "restarted"
    ROBLOX_RESTARTED = "roblox_restarted"
    SHUT_DOWN = "shut_down"
    UNSPECIFIED = "unspecified"

    def __str__(self) -> str:
        return str(self.value)
