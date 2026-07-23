from enum import Enum


class HomepageThumbnailStatus(str, Enum):
    ACTIVE = "Active"
    SPAMMY = "Spammy"

    def __str__(self) -> str:
        return str(self.value)
