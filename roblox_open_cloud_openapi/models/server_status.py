from enum import Enum


class ServerStatus(str, Enum):
    ACTIVE = "active"
    CRASHED = "crashed"
    MODERATED = "moderated"
    OUT_OF_MEMORY = "out_of_memory"
    RESTARTED = "restarted"
    ROBLOX_RESTARTED = "roblox_restarted"
    SHUT_DOWN = "shut_down"

    def __str__(self) -> str:
        return str(self.value)
