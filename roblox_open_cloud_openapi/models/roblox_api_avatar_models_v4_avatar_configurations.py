from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_avatar_thumbnail_customization_model import (
        RobloxApiAvatarModelsAvatarThumbnailCustomizationModel,
    )
    from ..models.roblox_api_avatar_models_emote_response_model import RobloxApiAvatarModelsEmoteResponseModel
    from ..models.roblox_api_avatar_models_v4_avatar_background_model import (
        RobloxApiAvatarModelsV4AvatarBackgroundModel,
    )
    from ..models.roblox_api_avatar_models_v4_avatar_profile_frame_model import (
        RobloxApiAvatarModelsV4AvatarProfileFrameModel,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4AvatarConfigurations")


@_attrs_define
class RobloxApiAvatarModelsV4AvatarConfigurations:
    """Avatar config details.

    Attributes:
        emotes (list[RobloxApiAvatarModelsEmoteResponseModel] | Unset): The emotes on the character.
        background (RobloxApiAvatarModelsV4AvatarBackgroundModel | Unset): A model containing avatar background data.
        thumbnail_customizations (list[RobloxApiAvatarModelsAvatarThumbnailCustomizationModel] | Unset): List of
            customizations set for this avatar. At most one per thumbnail type (Closeup, FullBody).
        profile_frame (RobloxApiAvatarModelsV4AvatarProfileFrameModel | Unset): A model containing avatar profile frame
            data.
    """

    emotes: list[RobloxApiAvatarModelsEmoteResponseModel] | Unset = UNSET
    background: RobloxApiAvatarModelsV4AvatarBackgroundModel | Unset = UNSET
    thumbnail_customizations: list[RobloxApiAvatarModelsAvatarThumbnailCustomizationModel] | Unset = UNSET
    profile_frame: RobloxApiAvatarModelsV4AvatarProfileFrameModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        emotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emotes, Unset):
            emotes = []
            for emotes_item_data in self.emotes:
                emotes_item = emotes_item_data.to_dict()
                emotes.append(emotes_item)

        background: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background, Unset):
            background = self.background.to_dict()

        thumbnail_customizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.thumbnail_customizations, Unset):
            thumbnail_customizations = []
            for thumbnail_customizations_item_data in self.thumbnail_customizations:
                thumbnail_customizations_item = thumbnail_customizations_item_data.to_dict()
                thumbnail_customizations.append(thumbnail_customizations_item)

        profile_frame: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile_frame, Unset):
            profile_frame = self.profile_frame.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if emotes is not UNSET:
            field_dict["emotes"] = emotes
        if background is not UNSET:
            field_dict["background"] = background
        if thumbnail_customizations is not UNSET:
            field_dict["thumbnailCustomizations"] = thumbnail_customizations
        if profile_frame is not UNSET:
            field_dict["profileFrame"] = profile_frame

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_avatar_thumbnail_customization_model import (
            RobloxApiAvatarModelsAvatarThumbnailCustomizationModel,
        )
        from ..models.roblox_api_avatar_models_emote_response_model import RobloxApiAvatarModelsEmoteResponseModel
        from ..models.roblox_api_avatar_models_v4_avatar_background_model import (
            RobloxApiAvatarModelsV4AvatarBackgroundModel,
        )
        from ..models.roblox_api_avatar_models_v4_avatar_profile_frame_model import (
            RobloxApiAvatarModelsV4AvatarProfileFrameModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _emotes = d.pop("emotes", UNSET)
        emotes: list[RobloxApiAvatarModelsEmoteResponseModel] | Unset = UNSET
        if _emotes is not UNSET:
            emotes = []
            for emotes_item_data in _emotes:
                emotes_item = RobloxApiAvatarModelsEmoteResponseModel.from_dict(emotes_item_data)

                emotes.append(emotes_item)

        _background = d.pop("background", UNSET)
        background: RobloxApiAvatarModelsV4AvatarBackgroundModel | Unset
        if isinstance(_background, Unset):
            background = UNSET
        else:
            background = RobloxApiAvatarModelsV4AvatarBackgroundModel.from_dict(_background)

        _thumbnail_customizations = d.pop("thumbnailCustomizations", UNSET)
        thumbnail_customizations: list[RobloxApiAvatarModelsAvatarThumbnailCustomizationModel] | Unset = UNSET
        if _thumbnail_customizations is not UNSET:
            thumbnail_customizations = []
            for thumbnail_customizations_item_data in _thumbnail_customizations:
                thumbnail_customizations_item = RobloxApiAvatarModelsAvatarThumbnailCustomizationModel.from_dict(
                    thumbnail_customizations_item_data
                )

                thumbnail_customizations.append(thumbnail_customizations_item)

        _profile_frame = d.pop("profileFrame", UNSET)
        profile_frame: RobloxApiAvatarModelsV4AvatarProfileFrameModel | Unset
        if isinstance(_profile_frame, Unset):
            profile_frame = UNSET
        else:
            profile_frame = RobloxApiAvatarModelsV4AvatarProfileFrameModel.from_dict(_profile_frame)

        roblox_api_avatar_models_v4_avatar_configurations = cls(
            emotes=emotes,
            background=background,
            thumbnail_customizations=thumbnail_customizations,
            profile_frame=profile_frame,
        )

        return roblox_api_avatar_models_v4_avatar_configurations
