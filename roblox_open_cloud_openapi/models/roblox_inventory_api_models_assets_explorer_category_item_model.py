from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_inventory_api_models_assets_explorer_category_item_model_type import (
    RobloxInventoryApiModelsAssetsExplorerCategoryItemModelType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxInventoryApiModelsAssetsExplorerCategoryItemModel")


@_attrs_define
class RobloxInventoryApiModelsAssetsExplorerCategoryItemModel:
    """
    Attributes:
        name (str | Unset):
        display_name (str | Unset):
        filter_ (str | Unset):
        id (int | Unset):
        type_ (RobloxInventoryApiModelsAssetsExplorerCategoryItemModelType | Unset): Describes what type an
            AssetsExplorerCategoryItemModel contains ['AssetType' = 0, 'Bundle' = 1, 'Outfit' = 2, 'Set' = 3, 'Avatar' = 4]
        category_type (str | Unset):
    """

    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    filter_: str | Unset = UNSET
    id: int | Unset = UNSET
    type_: RobloxInventoryApiModelsAssetsExplorerCategoryItemModelType | Unset = UNSET
    category_type: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        filter_ = self.filter_

        id = self.id

        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        category_type = self.category_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if category_type is not UNSET:
            field_dict["categoryType"] = category_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        filter_ = d.pop("filter", UNSET)

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RobloxInventoryApiModelsAssetsExplorerCategoryItemModelType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxInventoryApiModelsAssetsExplorerCategoryItemModelType(_type_)

        category_type = d.pop("categoryType", UNSET)

        roblox_inventory_api_models_assets_explorer_category_item_model = cls(
            name=name,
            display_name=display_name,
            filter_=filter_,
            id=id,
            type_=type_,
            category_type=category_type,
        )

        return roblox_inventory_api_models_assets_explorer_category_item_model
