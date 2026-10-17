from enum import StrEnum


class MatchmakingAttributeValueType(StrEnum):
    BOOL = "Bool"
    INVALID = "Invalid"
    NUMBER = "Number"
    STRING = "String"

    def __str__(self) -> str:
        return str(self.value)
