from enum import StrEnum


class InventoryItemCollectibleDetailsInstanceState(StrEnum):
    AVAILABLE = "AVAILABLE"
    COLLECTIBLE_ITEM_INSTANCE_STATE_UNSPECIFIED = "COLLECTIBLE_ITEM_INSTANCE_STATE_UNSPECIFIED"
    HOLD = "HOLD"

    def __str__(self) -> str:
        return str(self.value)
