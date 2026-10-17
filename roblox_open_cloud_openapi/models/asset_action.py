from enum import StrEnum


class AssetAction(StrEnum):
    COPYFROMRCC = "CopyFromRcc"
    DOWNLOAD = "Download"
    EDIT = "Edit"
    INVALID = "Invalid"
    UPDATEFROMRCC = "UpdateFromRcc"
    USE = "Use"

    def __str__(self) -> str:
        return str(self.value)
