from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_inventory_api_models_assets_explorer_category_item_model import (
        RobloxInventoryApiModelsAssetsExplorerCategoryItemModel,
    )


T = TypeVar("T", bound="RobloxInventoryApiModelsAssetsExplorerCategoryModel")


@_attrs_define
class RobloxInventoryApiModelsAssetsExplorerCategoryModel:
    """
    Attributes:
        name (str | Unset):
        display_name (str | Unset):
        category_type (str | Unset):
        items (list[RobloxInventoryApiModelsAssetsExplorerCategoryItemModel] | Unset):
    """

    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    category_type: str | Unset = UNSET
    items: list[RobloxInventoryApiModelsAssetsExplorerCategoryItemModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        category_type = self.category_type

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if category_type is not UNSET:
            field_dict["categoryType"] = category_type
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_inventory_api_models_assets_explorer_category_item_model import (
            RobloxInventoryApiModelsAssetsExplorerCategoryItemModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        category_type = d.pop("categoryType", UNSET)

        _items = d.pop("items", UNSET)
        items: list[RobloxInventoryApiModelsAssetsExplorerCategoryItemModel] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RobloxInventoryApiModelsAssetsExplorerCategoryItemModel.from_dict(items_item_data)

                items.append(items_item)

        roblox_inventory_api_models_assets_explorer_category_model = cls(
            name=name,
            display_name=display_name,
            category_type=category_type,
            items=items,
        )

        return roblox_inventory_api_models_assets_explorer_category_model
