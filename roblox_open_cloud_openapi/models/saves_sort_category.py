from enum import Enum


class SavesSortCategory(str, Enum):
    CREATOR = "Creator"
    DATE_SAVED = "DateSaved"
    LAST_MODIFIED = "LastModified"
    NAME = "Name"
    PRICE = "Price"
    RATINGS = "Ratings"
    TARGET_TYPE = "TargetType"

    def __str__(self) -> str:
        return str(self.value)
