from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_avatar_thumbnail_customization_model_thumbnail_type import (
    RobloxApiAvatarModelsAvatarThumbnailCustomizationModelThumbnailType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_avatar_thumbnail_customization_camera_model import (
        RobloxApiAvatarModelsAvatarThumbnailCustomizationCameraModel,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsAvatarThumbnailCustomizationModel")


@_attrs_define
class RobloxApiAvatarModelsAvatarThumbnailCustomizationModel:
    """A model describing a single avatar thumbnail customization.

    Attributes:
        thumbnail_type (RobloxApiAvatarModelsAvatarThumbnailCustomizationModelThumbnailType | Unset): What type of 2D
            thumbnail are we customizing: |Closeup, FullBody.
        emote_asset_id (int | Unset): What emote are we using to pose the avatar in the thumbnail.
        camera (RobloxApiAvatarModelsAvatarThumbnailCustomizationCameraModel | Unset): A model describing a the camera
            details for a single avatar thumbnail customization.
    """

    thumbnail_type: RobloxApiAvatarModelsAvatarThumbnailCustomizationModelThumbnailType | Unset = UNSET
    emote_asset_id: int | Unset = UNSET
    camera: RobloxApiAvatarModelsAvatarThumbnailCustomizationCameraModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        thumbnail_type: int | Unset = UNSET
        if not isinstance(self.thumbnail_type, Unset):
            thumbnail_type = self.thumbnail_type.value

        emote_asset_id = self.emote_asset_id

        camera: dict[str, Any] | Unset = UNSET
        if not isinstance(self.camera, Unset):
            camera = self.camera.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if thumbnail_type is not UNSET:
            field_dict["thumbnailType"] = thumbnail_type
        if emote_asset_id is not UNSET:
            field_dict["emoteAssetId"] = emote_asset_id
        if camera is not UNSET:
            field_dict["camera"] = camera

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_avatar_thumbnail_customization_camera_model import (
            RobloxApiAvatarModelsAvatarThumbnailCustomizationCameraModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _thumbnail_type = d.pop("thumbnailType", UNSET)
        thumbnail_type: RobloxApiAvatarModelsAvatarThumbnailCustomizationModelThumbnailType | Unset
        if isinstance(_thumbnail_type, Unset):
            thumbnail_type = UNSET
        else:
            thumbnail_type = RobloxApiAvatarModelsAvatarThumbnailCustomizationModelThumbnailType(_thumbnail_type)

        emote_asset_id = d.pop("emoteAssetId", UNSET)

        _camera = d.pop("camera", UNSET)
        camera: RobloxApiAvatarModelsAvatarThumbnailCustomizationCameraModel | Unset
        if isinstance(_camera, Unset):
            camera = UNSET
        else:
            camera = RobloxApiAvatarModelsAvatarThumbnailCustomizationCameraModel.from_dict(_camera)

        roblox_api_avatar_models_avatar_thumbnail_customization_model = cls(
            thumbnail_type=thumbnail_type,
            emote_asset_id=emote_asset_id,
            camera=camera,
        )

        return roblox_api_avatar_models_avatar_thumbnail_customization_model
