from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
    from ..models.roblox_api_avatar_models_invalid_background_response import (
        RobloxApiAvatarModelsInvalidBackgroundResponse,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4ResponseOutfitValidationResultV4")


@_attrs_define
class RobloxApiAvatarModelsV4ResponseOutfitValidationResultV4:
    """Validation details for outfit mutation responses when one or more inputs could not be applied.

    Attributes:
        unworn_assets (list[RobloxApiAvatarModelsAssetModelV2] | Unset): Assets that could not be worn.
        invalid_background (list[RobloxApiAvatarModelsInvalidBackgroundResponse] | Unset): Background assets that could
            not be applied.
    """

    unworn_assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
    invalid_background: list[RobloxApiAvatarModelsInvalidBackgroundResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        unworn_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unworn_assets, Unset):
            unworn_assets = []
            for unworn_assets_item_data in self.unworn_assets:
                unworn_assets_item = unworn_assets_item_data.to_dict()
                unworn_assets.append(unworn_assets_item)

        invalid_background: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_background, Unset):
            invalid_background = []
            for invalid_background_item_data in self.invalid_background:
                invalid_background_item = invalid_background_item_data.to_dict()
                invalid_background.append(invalid_background_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if unworn_assets is not UNSET:
            field_dict["unwornAssets"] = unworn_assets
        if invalid_background is not UNSET:
            field_dict["invalidBackground"] = invalid_background

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
        from ..models.roblox_api_avatar_models_invalid_background_response import (
            RobloxApiAvatarModelsInvalidBackgroundResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _unworn_assets = d.pop("unwornAssets", UNSET)
        unworn_assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
        if _unworn_assets is not UNSET:
            unworn_assets = []
            for unworn_assets_item_data in _unworn_assets:
                unworn_assets_item = RobloxApiAvatarModelsAssetModelV2.from_dict(unworn_assets_item_data)

                unworn_assets.append(unworn_assets_item)

        _invalid_background = d.pop("invalidBackground", UNSET)
        invalid_background: list[RobloxApiAvatarModelsInvalidBackgroundResponse] | Unset = UNSET
        if _invalid_background is not UNSET:
            invalid_background = []
            for invalid_background_item_data in _invalid_background:
                invalid_background_item = RobloxApiAvatarModelsInvalidBackgroundResponse.from_dict(
                    invalid_background_item_data
                )

                invalid_background.append(invalid_background_item)

        roblox_api_avatar_models_v4_response_outfit_validation_result_v4 = cls(
            unworn_assets=unworn_assets,
            invalid_background=invalid_background,
        )

        return roblox_api_avatar_models_v4_response_outfit_validation_result_v4
