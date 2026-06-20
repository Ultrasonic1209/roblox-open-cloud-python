from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiBundleItemDetailModelV2")


@_attrs_define
class RobloxCatalogApiBundleItemDetailModelV2:
    """The is the beta (non game-engine) version of BundleItemDetailModel for internal consumption on Roblox web and
    universal-app.

        Attributes:
            owned (bool | Unset):
            id (int | Unset):
            name (str | Unset):
            type_ (str | Unset):
            supports_head_shapes (bool | Unset): Whether the bundle item supports head shapes.
            asset_type (int | Unset): The asset type of the bundle item, if it's an asset.
    """

    owned: bool | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    supports_head_shapes: bool | Unset = UNSET
    asset_type: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        owned = self.owned

        id = self.id

        name = self.name

        type_ = self.type_

        supports_head_shapes = self.supports_head_shapes

        asset_type = self.asset_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if owned is not UNSET:
            field_dict["owned"] = owned
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if supports_head_shapes is not UNSET:
            field_dict["supportsHeadShapes"] = supports_head_shapes
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        owned = d.pop("owned", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        supports_head_shapes = d.pop("supportsHeadShapes", UNSET)

        asset_type = d.pop("assetType", UNSET)

        roblox_catalog_api_bundle_item_detail_model_v2 = cls(
            owned=owned,
            id=id,
            name=name,
            type_=type_,
            supports_head_shapes=supports_head_shapes,
            asset_type=asset_type,
        )

        return roblox_catalog_api_bundle_item_detail_model_v2
