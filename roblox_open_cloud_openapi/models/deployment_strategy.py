from enum import StrEnum


class DeploymentStrategy(StrEnum):
    GRADUAL_ROLLOUT = "GradualRollout"
    IMMEDIATE = "Immediate"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
