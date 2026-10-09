from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
    from ..models.roblox_api_avatar_models_v4_response_avatar_validation_result_v4 import (
        RobloxApiAvatarModelsV4ResponseAvatarValidationResultV4,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4")


@_attrs_define
class RobloxApiAvatarModelsV4ResponseUpdateAvatarDefinitionResponseV4:
    """Response model for update avatar (V4).

    Attributes:
        success (bool | Unset): Whether all requested changes were successfully applied.
        invalid_assets (list[RobloxApiAvatarModelsAssetModelV2] | Unset): Temporary top-level mirror of
            Roblox.Api.Avatar.Models.V4.Response.AvatarValidationResultV4.InvalidAssets to unblock
            clients that still read `invalidAssets` at the response root during backgrounds rollout.
            Prefer Roblox.Api.Avatar.Models.V4.Response.UpdateAvatarDefinitionResponseV4.Validation.Roblox.Api.Avatar.Models
            .V4.Response.AvatarValidationResultV4.InvalidAssets.
            Will be reverted once the engine fix is fully deployed.
        validation (RobloxApiAvatarModelsV4ResponseAvatarValidationResultV4 | Unset): Validation details for avatar
            mutation responses when one or more inputs could not be applied.
    """

    success: bool | Unset = UNSET
    invalid_assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
    validation: RobloxApiAvatarModelsV4ResponseAvatarValidationResultV4 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        invalid_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_assets, Unset):
            invalid_assets = []
            for invalid_assets_item_data in self.invalid_assets:
                invalid_assets_item = invalid_assets_item_data.to_dict()
                invalid_assets.append(invalid_assets_item)

        validation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if invalid_assets is not UNSET:
            field_dict["invalidAssets"] = invalid_assets
        if validation is not UNSET:
            field_dict["validation"] = validation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
        from ..models.roblox_api_avatar_models_v4_response_avatar_validation_result_v4 import (
            RobloxApiAvatarModelsV4ResponseAvatarValidationResultV4,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        success = d.pop("success", UNSET)

        _invalid_assets = d.pop("invalidAssets", UNSET)
        invalid_assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
        if _invalid_assets is not UNSET:
            invalid_assets = []
            for invalid_assets_item_data in _invalid_assets:
                invalid_assets_item = RobloxApiAvatarModelsAssetModelV2.from_dict(invalid_assets_item_data)

                invalid_assets.append(invalid_assets_item)

        _validation = d.pop("validation", UNSET)
        validation: RobloxApiAvatarModelsV4ResponseAvatarValidationResultV4 | Unset
        if isinstance(_validation, Unset):
            validation = UNSET
        else:
            validation = RobloxApiAvatarModelsV4ResponseAvatarValidationResultV4.from_dict(_validation)

        roblox_api_avatar_models_v4_response_update_avatar_definition_response_v4 = cls(
            success=success,
            invalid_assets=invalid_assets,
            validation=validation,
        )

        return roblox_api_avatar_models_v4_response_update_avatar_definition_response_v4
