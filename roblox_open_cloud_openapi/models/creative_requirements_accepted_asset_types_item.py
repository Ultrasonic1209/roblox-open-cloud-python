from enum import StrEnum


class CreativeRequirementsAcceptedAssetTypesItem(StrEnum):
    IMAGE = "IMAGE"

    def __str__(self) -> str:
        return str(self.value)
