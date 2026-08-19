from enum import Enum


class ExperimentProductType(str, Enum):
    IN_GAME_CONFIGS = "EXPERIMENT_PRODUCT_TYPE_IN_GAME_CONFIGS"
    MATCHMAKING = "EXPERIMENT_PRODUCT_TYPE_MATCHMAKING"

    def __str__(self) -> str:
        return str(self.value)
