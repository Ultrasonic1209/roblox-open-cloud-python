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
    from ..models.roblox_api_avatar_models_invalid_emote_response_model import (
        RobloxApiAvatarModelsInvalidEmoteResponseModel,
    )
    from ..models.roblox_api_avatar_models_invalid_profile_frame_response import (
        RobloxApiAvatarModelsInvalidProfileFrameResponse,
    )
    from ..models.roblox_api_avatar_models_v4_response_invalid_thumbnail_customization_response import (
        RobloxApiAvatarModelsV4ResponseInvalidThumbnailCustomizationResponse,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4ResponseAvatarValidationResultV4")


@_attrs_define
class RobloxApiAvatarModelsV4ResponseAvatarValidationResultV4:
    """Validation details for avatar mutation responses when one or more inputs could not be applied.

    Attributes:
        invalid_assets (list[RobloxApiAvatarModelsAssetModelV2] | Unset): Assets that could not be worn.
        invalid_background (list[RobloxApiAvatarModelsInvalidBackgroundResponse] | Unset): Background assets that could
            not be applied.
        invalid_profile_frame (list[RobloxApiAvatarModelsInvalidProfileFrameResponse] | Unset): Profile frame assets
            that could not be applied.
        invalid_emotes (list[RobloxApiAvatarModelsInvalidEmoteResponseModel] | Unset): Emotes that could not be
            equipped.
        invalid_thumbnail_customizations (list[RobloxApiAvatarModelsV4ResponseInvalidThumbnailCustomizationResponse] |
            Unset): Thumbnail customizations that could not be applied.
    """

    invalid_assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
    invalid_background: list[RobloxApiAvatarModelsInvalidBackgroundResponse] | Unset = UNSET
    invalid_profile_frame: list[RobloxApiAvatarModelsInvalidProfileFrameResponse] | Unset = UNSET
    invalid_emotes: list[RobloxApiAvatarModelsInvalidEmoteResponseModel] | Unset = UNSET
    invalid_thumbnail_customizations: (
        list[RobloxApiAvatarModelsV4ResponseInvalidThumbnailCustomizationResponse] | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        invalid_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_assets, Unset):
            invalid_assets = []
            for invalid_assets_item_data in self.invalid_assets:
                invalid_assets_item = invalid_assets_item_data.to_dict()
                invalid_assets.append(invalid_assets_item)

        invalid_background: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_background, Unset):
            invalid_background = []
            for invalid_background_item_data in self.invalid_background:
                invalid_background_item = invalid_background_item_data.to_dict()
                invalid_background.append(invalid_background_item)

        invalid_profile_frame: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_profile_frame, Unset):
            invalid_profile_frame = []
            for invalid_profile_frame_item_data in self.invalid_profile_frame:
                invalid_profile_frame_item = invalid_profile_frame_item_data.to_dict()
                invalid_profile_frame.append(invalid_profile_frame_item)

        invalid_emotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_emotes, Unset):
            invalid_emotes = []
            for invalid_emotes_item_data in self.invalid_emotes:
                invalid_emotes_item = invalid_emotes_item_data.to_dict()
                invalid_emotes.append(invalid_emotes_item)

        invalid_thumbnail_customizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_thumbnail_customizations, Unset):
            invalid_thumbnail_customizations = []
            for invalid_thumbnail_customizations_item_data in self.invalid_thumbnail_customizations:
                invalid_thumbnail_customizations_item = invalid_thumbnail_customizations_item_data.to_dict()
                invalid_thumbnail_customizations.append(invalid_thumbnail_customizations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if invalid_assets is not UNSET:
            field_dict["invalidAssets"] = invalid_assets
        if invalid_background is not UNSET:
            field_dict["invalidBackground"] = invalid_background
        if invalid_profile_frame is not UNSET:
            field_dict["invalidProfileFrame"] = invalid_profile_frame
        if invalid_emotes is not UNSET:
            field_dict["invalidEmotes"] = invalid_emotes
        if invalid_thumbnail_customizations is not UNSET:
            field_dict["invalidThumbnailCustomizations"] = invalid_thumbnail_customizations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_model_v2 import RobloxApiAvatarModelsAssetModelV2
        from ..models.roblox_api_avatar_models_invalid_background_response import (
            RobloxApiAvatarModelsInvalidBackgroundResponse,
        )
        from ..models.roblox_api_avatar_models_invalid_emote_response_model import (
            RobloxApiAvatarModelsInvalidEmoteResponseModel,
        )
        from ..models.roblox_api_avatar_models_invalid_profile_frame_response import (
            RobloxApiAvatarModelsInvalidProfileFrameResponse,
        )
        from ..models.roblox_api_avatar_models_v4_response_invalid_thumbnail_customization_response import (
            RobloxApiAvatarModelsV4ResponseInvalidThumbnailCustomizationResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _invalid_assets = d.pop("invalidAssets", UNSET)
        invalid_assets: list[RobloxApiAvatarModelsAssetModelV2] | Unset = UNSET
        if _invalid_assets is not UNSET:
            invalid_assets = []
            for invalid_assets_item_data in _invalid_assets:
                invalid_assets_item = RobloxApiAvatarModelsAssetModelV2.from_dict(invalid_assets_item_data)

                invalid_assets.append(invalid_assets_item)

        _invalid_background = d.pop("invalidBackground", UNSET)
        invalid_background: list[RobloxApiAvatarModelsInvalidBackgroundResponse] | Unset = UNSET
        if _invalid_background is not UNSET:
            invalid_background = []
            for invalid_background_item_data in _invalid_background:
                invalid_background_item = RobloxApiAvatarModelsInvalidBackgroundResponse.from_dict(
                    invalid_background_item_data
                )

                invalid_background.append(invalid_background_item)

        _invalid_profile_frame = d.pop("invalidProfileFrame", UNSET)
        invalid_profile_frame: list[RobloxApiAvatarModelsInvalidProfileFrameResponse] | Unset = UNSET
        if _invalid_profile_frame is not UNSET:
            invalid_profile_frame = []
            for invalid_profile_frame_item_data in _invalid_profile_frame:
                invalid_profile_frame_item = RobloxApiAvatarModelsInvalidProfileFrameResponse.from_dict(
                    invalid_profile_frame_item_data
                )

                invalid_profile_frame.append(invalid_profile_frame_item)

        _invalid_emotes = d.pop("invalidEmotes", UNSET)
        invalid_emotes: list[RobloxApiAvatarModelsInvalidEmoteResponseModel] | Unset = UNSET
        if _invalid_emotes is not UNSET:
            invalid_emotes = []
            for invalid_emotes_item_data in _invalid_emotes:
                invalid_emotes_item = RobloxApiAvatarModelsInvalidEmoteResponseModel.from_dict(invalid_emotes_item_data)

                invalid_emotes.append(invalid_emotes_item)

        _invalid_thumbnail_customizations = d.pop("invalidThumbnailCustomizations", UNSET)
        invalid_thumbnail_customizations: (
            list[RobloxApiAvatarModelsV4ResponseInvalidThumbnailCustomizationResponse] | Unset
        ) = UNSET
        if _invalid_thumbnail_customizations is not UNSET:
            invalid_thumbnail_customizations = []
            for invalid_thumbnail_customizations_item_data in _invalid_thumbnail_customizations:
                invalid_thumbnail_customizations_item = (
                    RobloxApiAvatarModelsV4ResponseInvalidThumbnailCustomizationResponse.from_dict(
                        invalid_thumbnail_customizations_item_data
                    )
                )

                invalid_thumbnail_customizations.append(invalid_thumbnail_customizations_item)

        roblox_api_avatar_models_v4_response_avatar_validation_result_v4 = cls(
            invalid_assets=invalid_assets,
            invalid_background=invalid_background,
            invalid_profile_frame=invalid_profile_frame,
            invalid_emotes=invalid_emotes,
            invalid_thumbnail_customizations=invalid_thumbnail_customizations,
        )

        return roblox_api_avatar_models_v4_response_avatar_validation_result_v4
