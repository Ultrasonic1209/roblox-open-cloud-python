from enum import StrEnum


class GetV2UsersUserIdTradableItemsSortBy(StrEnum):
    ACQUISITIONTIME = "AcquisitionTime"
    CREATIONTIME = "CreationTime"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
