from enum import StrEnum


class InternalPublicV1CreativeAssetType(StrEnum):
    IMAGE = "IMAGE"

    def __str__(self) -> str:
        return str(self.value)
