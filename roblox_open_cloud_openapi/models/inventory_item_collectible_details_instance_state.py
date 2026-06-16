from enum import Enum


class InventoryItemCollectibleDetailsInstanceState(str, Enum):
    AVAILABLE = "AVAILABLE"
    COLLECTIBLE_ITEM_INSTANCE_STATE_UNSPECIFIED = "COLLECTIBLE_ITEM_INSTANCE_STATE_UNSPECIFIED"
    HOLD = "HOLD"

    def __str__(self) -> str:
        return str(self.value)
