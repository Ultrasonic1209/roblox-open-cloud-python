from enum import Enum


class InternalPublicV1CreativeAssetType(str, Enum):
    IMAGE = "IMAGE"

    def __str__(self) -> str:
        return str(self.value)
