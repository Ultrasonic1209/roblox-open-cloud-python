from enum import StrEnum


class ConfigVariantType(StrEnum):
    CONDITIONAL = "conditional"

    def __str__(self) -> str:
        return str(self.value)
