from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_avatar_thumbnail_customization_model import (
        RobloxApiAvatarModelsAvatarThumbnailCustomizationModel,
    )
    from ..models.roblox_api_avatar_models_emote_request_model import RobloxApiAvatarModelsEmoteRequestModel
    from ..models.roblox_api_avatar_models_v4_avatar_background_request_model import (
        RobloxApiAvatarModelsV4AvatarBackgroundRequestModel,
    )
    from ..models.roblox_api_avatar_models_v4_avatar_profile_frame_request_model import (
        RobloxApiAvatarModelsV4AvatarProfileFrameRequestModel,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4UpdateAvatarConfig")


@_attrs_define
class RobloxApiAvatarModelsV4UpdateAvatarConfig:
    """A model containing avatar config fields to update.

    Attributes:
        emote_request_models (list[RobloxApiAvatarModelsEmoteRequestModel] | Unset): The avatar's emotes.
        thumbnail_customization_models (list[RobloxApiAvatarModelsAvatarThumbnailCustomizationModel] | Unset): The
            avatar's thumbnail customizations.
        background_request_model (RobloxApiAvatarModelsV4AvatarBackgroundRequestModel | Unset): A model which contains
            the asset id of the background. This can be
            extended to have more attributes in the future.
        profile_frame_request_model (RobloxApiAvatarModelsV4AvatarProfileFrameRequestModel | Unset): A model which
            contains the asset id of the profile frame.
    """

    emote_request_models: list[RobloxApiAvatarModelsEmoteRequestModel] | Unset = UNSET
    thumbnail_customization_models: list[RobloxApiAvatarModelsAvatarThumbnailCustomizationModel] | Unset = UNSET
    background_request_model: RobloxApiAvatarModelsV4AvatarBackgroundRequestModel | Unset = UNSET
    profile_frame_request_model: RobloxApiAvatarModelsV4AvatarProfileFrameRequestModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        emote_request_models: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emote_request_models, Unset):
            emote_request_models = []
            for emote_request_models_item_data in self.emote_request_models:
                emote_request_models_item = emote_request_models_item_data.to_dict()
                emote_request_models.append(emote_request_models_item)

        thumbnail_customization_models: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.thumbnail_customization_models, Unset):
            thumbnail_customization_models = []
            for thumbnail_customization_models_item_data in self.thumbnail_customization_models:
                thumbnail_customization_models_item = thumbnail_customization_models_item_data.to_dict()
                thumbnail_customization_models.append(thumbnail_customization_models_item)

        background_request_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_request_model, Unset):
            background_request_model = self.background_request_model.to_dict()

        profile_frame_request_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile_frame_request_model, Unset):
            profile_frame_request_model = self.profile_frame_request_model.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if emote_request_models is not UNSET:
            field_dict["emoteRequestModels"] = emote_request_models
        if thumbnail_customization_models is not UNSET:
            field_dict["thumbnailCustomizationModels"] = thumbnail_customization_models
        if background_request_model is not UNSET:
            field_dict["backgroundRequestModel"] = background_request_model
        if profile_frame_request_model is not UNSET:
            field_dict["profileFrameRequestModel"] = profile_frame_request_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_avatar_thumbnail_customization_model import (
            RobloxApiAvatarModelsAvatarThumbnailCustomizationModel,
        )
        from ..models.roblox_api_avatar_models_emote_request_model import RobloxApiAvatarModelsEmoteRequestModel
        from ..models.roblox_api_avatar_models_v4_avatar_background_request_model import (
            RobloxApiAvatarModelsV4AvatarBackgroundRequestModel,
        )
        from ..models.roblox_api_avatar_models_v4_avatar_profile_frame_request_model import (
            RobloxApiAvatarModelsV4AvatarProfileFrameRequestModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _emote_request_models = d.pop("emoteRequestModels", UNSET)
        emote_request_models: list[RobloxApiAvatarModelsEmoteRequestModel] | Unset = UNSET
        if _emote_request_models is not UNSET:
            emote_request_models = []
            for emote_request_models_item_data in _emote_request_models:
                emote_request_models_item = RobloxApiAvatarModelsEmoteRequestModel.from_dict(
                    emote_request_models_item_data
                )

                emote_request_models.append(emote_request_models_item)

        _thumbnail_customization_models = d.pop("thumbnailCustomizationModels", UNSET)
        thumbnail_customization_models: list[RobloxApiAvatarModelsAvatarThumbnailCustomizationModel] | Unset = UNSET
        if _thumbnail_customization_models is not UNSET:
            thumbnail_customization_models = []
            for thumbnail_customization_models_item_data in _thumbnail_customization_models:
                thumbnail_customization_models_item = RobloxApiAvatarModelsAvatarThumbnailCustomizationModel.from_dict(
                    thumbnail_customization_models_item_data
                )

                thumbnail_customization_models.append(thumbnail_customization_models_item)

        _background_request_model = d.pop("backgroundRequestModel", UNSET)
        background_request_model: RobloxApiAvatarModelsV4AvatarBackgroundRequestModel | Unset
        if isinstance(_background_request_model, Unset):
            background_request_model = UNSET
        else:
            background_request_model = RobloxApiAvatarModelsV4AvatarBackgroundRequestModel.from_dict(
                _background_request_model
            )

        _profile_frame_request_model = d.pop("profileFrameRequestModel", UNSET)
        profile_frame_request_model: RobloxApiAvatarModelsV4AvatarProfileFrameRequestModel | Unset
        if isinstance(_profile_frame_request_model, Unset):
            profile_frame_request_model = UNSET
        else:
            profile_frame_request_model = RobloxApiAvatarModelsV4AvatarProfileFrameRequestModel.from_dict(
                _profile_frame_request_model
            )

        roblox_api_avatar_models_v4_update_avatar_config = cls(
            emote_request_models=emote_request_models,
            thumbnail_customization_models=thumbnail_customization_models,
            background_request_model=background_request_model,
            profile_frame_request_model=profile_frame_request_model,
        )

        return roblox_api_avatar_models_v4_update_avatar_config
