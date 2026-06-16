from enum import Enum


class DeploymentStrategy(str, Enum):
    GRADUAL_ROLLOUT = "GradualRollout"
    IMMEDIATE = "Immediate"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
