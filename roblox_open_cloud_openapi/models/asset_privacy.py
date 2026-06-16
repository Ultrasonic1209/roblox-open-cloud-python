from enum import Enum


class AssetPrivacy(str, Enum):
    DEFAULT = "default"
    OPENUSE = "openUse"
    RESTRICTED = "restricted"

    def __str__(self) -> str:
        return str(self.value)
