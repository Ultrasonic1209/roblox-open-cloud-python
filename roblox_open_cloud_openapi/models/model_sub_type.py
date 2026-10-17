from enum import StrEnum


class ModelSubType(StrEnum):
    AD = "Ad"
    MATERIAL_PACK = "MaterialPack"
    PACKAGE = "Package"

    def __str__(self) -> str:
        return str(self.value)
