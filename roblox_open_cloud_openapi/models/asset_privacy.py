from enum import StrEnum


class AssetPrivacy(StrEnum):
    DEFAULT = "default"
    OPENUSE = "openUse"
    RESTRICTED = "restricted"

    def __str__(self) -> str:
        return str(self.value)
