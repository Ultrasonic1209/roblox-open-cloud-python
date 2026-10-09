from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2


T = TypeVar("T", bound="RobloxApiAvatarModelsV4AvatarBackgroundModel")


@_attrs_define
class RobloxApiAvatarModelsV4AvatarBackgroundModel:
    """A model containing avatar background data.

    Attributes:
        background_asset (RobloxApiAvatarModelsAssetModelV2 | Unset): A model containing details about an asset
            - V2: adds CurrentVersionId, AssetMetaModel
    """

    background_asset: RobloxApiAvatarModelsAssetModelV2 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        background_asset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_asset, Unset):
            background_asset = self.background_asset.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if background_asset is not UNSET:
            field_dict["backgroundAsset"] = background_asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _background_asset = d.pop("backgroundAsset", UNSET)
        background_asset: RobloxApiAvatarModelsAssetModelV2 | Unset
        if isinstance(_background_asset, Unset):
            background_asset = UNSET
        else:
            background_asset = RobloxApiAvatarModelsAssetModelV2.from_dict(_background_asset)

        roblox_api_avatar_models_v4_avatar_background_model = cls(
            background_asset=background_asset,
        )

        return roblox_api_avatar_models_v4_avatar_background_model
