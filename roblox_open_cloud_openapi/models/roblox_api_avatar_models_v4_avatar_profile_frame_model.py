from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2


T = TypeVar("T", bound="RobloxApiAvatarModelsV4AvatarProfileFrameModel")


@_attrs_define
class RobloxApiAvatarModelsV4AvatarProfileFrameModel:
    """A model containing avatar profile frame data.

    Attributes:
        frame_asset (RobloxApiAvatarModelsAssetModelV2 | Unset): A model containing details about an asset
            - V2: adds CurrentVersionId, AssetMetaModel
    """

    frame_asset: RobloxApiAvatarModelsAssetModelV2 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        frame_asset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.frame_asset, Unset):
            frame_asset = self.frame_asset.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if frame_asset is not UNSET:
            field_dict["frameAsset"] = frame_asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _frame_asset = d.pop("frameAsset", UNSET)
        frame_asset: RobloxApiAvatarModelsAssetModelV2 | Unset
        if isinstance(_frame_asset, Unset):
            frame_asset = UNSET
        else:
            frame_asset = RobloxApiAvatarModelsAssetModelV2.from_dict(_frame_asset)

        roblox_api_avatar_models_v4_avatar_profile_frame_model = cls(
            frame_asset=frame_asset,
        )

        return roblox_api_avatar_models_v4_avatar_profile_frame_model
