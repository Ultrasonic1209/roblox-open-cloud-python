from enum import Enum


class ConfigVariantType(str, Enum):
    CONDITIONAL = "conditional"

    def __str__(self) -> str:
        return str(self.value)
