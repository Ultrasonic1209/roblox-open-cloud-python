from enum import Enum


class GetV2UsersUserIdTradableItemsSortBy(str, Enum):
    ACQUISITIONTIME = "AcquisitionTime"
    CREATIONTIME = "CreationTime"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
