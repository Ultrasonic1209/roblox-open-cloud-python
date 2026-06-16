from enum import Enum


class AssetAction(str, Enum):
    COPYFROMRCC = "CopyFromRcc"
    DOWNLOAD = "Download"
    EDIT = "Edit"
    INVALID = "Invalid"
    UPDATEFROMRCC = "UpdateFromRcc"
    USE = "Use"

    def __str__(self) -> str:
        return str(self.value)
