from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2


T = TypeVar("T", bound="RobloxApiAvatarModelsUpdateAvatarResponseModel")


@_attrs_define
class RobloxApiAvatarModelsUpdateAvatarResponseModel:
    """A model for update avatar responses.

    Attributes:
        invalid_assets (list[RobloxApiAvatarModelsAssetModelV2] | Unset): The assets that could not be worn
            Unlike invalidAssetIds, only contains assets that are wearable types.
        success (bool | Unset): Whether or not all the outfit contents were successfully worn.
    """

    invalid_assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
    success: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        invalid_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_assets, Unset):
            invalid_assets = []
            for invalid_assets_item_data in self.invalid_assets:
                invalid_assets_item = invalid_assets_item_data.to_dict()
                invalid_assets.append(invalid_assets_item)

        success = self.success

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if invalid_assets is not UNSET:
            field_dict["invalidAssets"] = invalid_assets
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _invalid_assets = d.pop("invalidAssets", UNSET)
        invalid_assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
        if _invalid_assets is not UNSET:
            invalid_assets = []
            for invalid_assets_item_data in _invalid_assets:
                invalid_assets_item = RobloxApiAvatarModelsAssetModelV2.from_dict(invalid_assets_item_data)

                invalid_assets.append(invalid_assets_item)

        success = d.pop("success", UNSET)

        roblox_api_avatar_models_update_avatar_response_model = cls(
            invalid_assets=invalid_assets,
            success=success,
        )

        return roblox_api_avatar_models_update_avatar_response_model
