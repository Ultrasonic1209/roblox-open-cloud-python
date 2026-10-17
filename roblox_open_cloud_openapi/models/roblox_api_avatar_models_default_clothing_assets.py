from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsDefaultClothingAssets")


@_attrs_define
class RobloxApiAvatarModelsDefaultClothingAssets:
    """A model containing details about avatar-related business rules

    Attributes:
        default_shirt_asset_ids (list[int] | Unset): List of asset Ids used to equip shirts for default clothing when
            the avatar appears nude.
        default_pant_asset_ids (list[int] | Unset): List of asset Ids used to equip pants for default clothing when the
            avatar appears nude.
    """

    default_shirt_asset_ids: list[int] | Unset = UNSET
    default_pant_asset_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        default_shirt_asset_ids: list[int] | Unset = UNSET
        if not isinstance(self.default_shirt_asset_ids, Unset):
            default_shirt_asset_ids = self.default_shirt_asset_ids

        default_pant_asset_ids: list[int] | Unset = UNSET
        if not isinstance(self.default_pant_asset_ids, Unset):
            default_pant_asset_ids = self.default_pant_asset_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if default_shirt_asset_ids is not UNSET:
            field_dict["defaultShirtAssetIds"] = default_shirt_asset_ids
        if default_pant_asset_ids is not UNSET:
            field_dict["defaultPantAssetIds"] = default_pant_asset_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_shirt_asset_ids = cast(list[int], d.pop("defaultShirtAssetIds", UNSET))

        default_pant_asset_ids = cast(list[int], d.pop("defaultPantAssetIds", UNSET))

        roblox_api_avatar_models_default_clothing_assets = cls(
            default_shirt_asset_ids=default_shirt_asset_ids,
            default_pant_asset_ids=default_pant_asset_ids,
        )

        return roblox_api_avatar_models_default_clothing_assets
