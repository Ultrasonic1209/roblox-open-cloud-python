from enum import StrEnum


class RobloxItemConfigurationApiModelsFolderFolderItemItemType(StrEnum):
    ASSET = "Asset"
    BUNDLE = "Bundle"
    FOLDER = "Folder"
    IECTOKEN = "IECToken"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
