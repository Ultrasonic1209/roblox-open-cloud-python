from enum import StrEnum


class UniverseAgeRating(StrEnum):
    AGE_RATING_13_PLUS = "AGE_RATING_13_PLUS"
    AGE_RATING_17_PLUS = "AGE_RATING_17_PLUS"
    AGE_RATING_9_PLUS = "AGE_RATING_9_PLUS"
    AGE_RATING_ALL = "AGE_RATING_ALL"
    AGE_RATING_UNSPECIFIED = "AGE_RATING_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
