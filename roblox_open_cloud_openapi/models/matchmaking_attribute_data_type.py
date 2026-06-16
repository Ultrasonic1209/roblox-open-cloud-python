from enum import Enum


class MatchmakingAttributeDataType(str, Enum):
    BOOL = "Bool"
    INVALID = "Invalid"
    NUMBER = "Number"
    STRING = "String"

    def __str__(self) -> str:
        return str(self.value)
