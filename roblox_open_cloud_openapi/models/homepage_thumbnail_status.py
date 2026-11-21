from enum import StrEnum


class HomepageThumbnailStatus(StrEnum):
    ACTIVE = "Active"
    SPAMMY = "Spammy"

    def __str__(self) -> str:
        return str(self.value)
