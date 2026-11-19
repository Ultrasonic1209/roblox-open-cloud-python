from enum import StrEnum


class AssetPrivacy(StrEnum):
    DEFAULT = "Default"
    OPENUSE = "OpenUse"
    RESTRICTED = "Restricted"
    UNSPECIFIED = "Unspecified"

    def __str__(self) -> str:
        return str(self.value)
