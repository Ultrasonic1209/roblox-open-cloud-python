from enum import Enum


class ExperimentState(str, Enum):
    CANCELLED = "EXPERIMENT_STATE_CANCELLED"
    COMPLETED = "EXPERIMENT_STATE_COMPLETED"
    DELETED = "EXPERIMENT_STATE_DELETED"
    DRAFT = "EXPERIMENT_STATE_DRAFT"
    RUNNING = "EXPERIMENT_STATE_RUNNING"
    SCHEDULED = "EXPERIMENT_STATE_SCHEDULED"

    def __str__(self) -> str:
        return str(self.value)
