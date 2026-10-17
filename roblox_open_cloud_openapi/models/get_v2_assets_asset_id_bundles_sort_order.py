from enum import StrEnum


class GetV2AssetsAssetIdBundlesSortOrder(StrEnum):
    ASC = "Asc"
    DESC = "Desc"

    def __str__(self) -> str:
        return str(self.value)
