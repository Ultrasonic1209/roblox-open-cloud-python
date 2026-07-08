from enum import Enum


class FilterOperation(str, Enum):
    GREATERTHAN = "GreaterThan"
    GREATERTHANOREQUAL = "GreaterThanOrEqual"
    IN = "In"
    LESSTHAN = "LessThan"
    LESSTHANOREQUAL = "LessThanOrEqual"
    MATCH = "Match"
    NOTIN = "NotIn"

    def __str__(self) -> str:
        return str(self.value)
