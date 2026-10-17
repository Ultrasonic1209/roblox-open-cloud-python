from enum import StrEnum


class SavesSortCategory(StrEnum):
    CREATOR = "Creator"
    DATE_SAVED = "DateSaved"
    LAST_MODIFIED = "LastModified"
    NAME = "Name"
    PRICE = "Price"
    RATINGS = "Ratings"
    TARGET_TYPE = "TargetType"

    def __str__(self) -> str:
        return str(self.value)
