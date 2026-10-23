from enum import StrEnum


class ListExperimentSortKey(StrEnum):
    LAST_MODIFIED_TIME = "LIST_EXPERIMENT_SORT_KEY_LAST_MODIFIED_TIME"
    NAME = "LIST_EXPERIMENT_SORT_KEY_NAME"
    RELEVANCE = "LIST_EXPERIMENT_SORT_KEY_RELEVANCE"
    START_TIME = "LIST_EXPERIMENT_SORT_KEY_START_TIME"

    def __str__(self) -> str:
        return str(self.value)
