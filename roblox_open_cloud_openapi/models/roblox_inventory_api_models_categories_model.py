from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_inventory_api_models_assets_explorer_category_model import (
        RobloxInventoryApiModelsAssetsExplorerCategoryModel,
    )


T = TypeVar("T", bound="RobloxInventoryApiModelsCategoriesModel")


@_attrs_define
class RobloxInventoryApiModelsCategoriesModel:
    """Model class that contains the categories of the Inventory or Favorites page

    Attributes:
        categories (list[RobloxInventoryApiModelsAssetsExplorerCategoryModel] | Unset): Categories to show up in
            Inventory or Favorites page
    """

    categories: list[RobloxInventoryApiModelsAssetsExplorerCategoryModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_inventory_api_models_assets_explorer_category_model import (
            RobloxInventoryApiModelsAssetsExplorerCategoryModel,
        )

        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: list[RobloxInventoryApiModelsAssetsExplorerCategoryModel] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = RobloxInventoryApiModelsAssetsExplorerCategoryModel.from_dict(categories_item_data)

                categories.append(categories_item)

        roblox_inventory_api_models_categories_model = cls(
            categories=categories,
        )

        return roblox_inventory_api_models_categories_model
