from enum import Enum


class ModelSubType(str, Enum):
    AD = "Ad"
    MATERIAL_PACK = "MaterialPack"
    PACKAGE = "Package"

    def __str__(self) -> str:
        return str(self.value)
