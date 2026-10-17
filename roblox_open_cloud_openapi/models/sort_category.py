from enum import StrEnum


class SortCategory(StrEnum):
    AUDIO_DURATION = "AudioDuration"
    CREATE_TIME = "CreateTime"
    RATINGS = "Ratings"
    RELEVANCE = "Relevance"
    TOP = "Top"
    TRENDING = "Trending"
    UPDATED_TIME = "UpdatedTime"

    def __str__(self) -> str:
        return str(self.value)
