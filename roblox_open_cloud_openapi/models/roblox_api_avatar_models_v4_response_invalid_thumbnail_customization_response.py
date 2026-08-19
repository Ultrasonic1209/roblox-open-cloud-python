from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_avatar_thumbnail_customization_model import (
        RobloxApiAvatarModelsAvatarThumbnailCustomizationModel,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4ResponseInvalidThumbnailCustomizationResponse")


@_attrs_define
class RobloxApiAvatarModelsV4ResponseInvalidThumbnailCustomizationResponse:
    """
    Attributes:
        thumbnail_customization_model (RobloxApiAvatarModelsAvatarThumbnailCustomizationModel | Unset): A model
            describing a single avatar thumbnail customization.
        error (str | Unset): The error associated with the thumbnail customization
    """

    thumbnail_customization_model: RobloxApiAvatarModelsAvatarThumbnailCustomizationModel | Unset = UNSET
    error: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        thumbnail_customization_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail_customization_model, Unset):
            thumbnail_customization_model = self.thumbnail_customization_model.to_dict()

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if thumbnail_customization_model is not UNSET:
            field_dict["ThumbnailCustomizationModel"] = thumbnail_customization_model
        if error is not UNSET:
            field_dict["Error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_avatar_thumbnail_customization_model import (
            RobloxApiAvatarModelsAvatarThumbnailCustomizationModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _thumbnail_customization_model = d.pop("ThumbnailCustomizationModel", UNSET)
        thumbnail_customization_model: RobloxApiAvatarModelsAvatarThumbnailCustomizationModel | Unset
        if isinstance(_thumbnail_customization_model, Unset):
            thumbnail_customization_model = UNSET
        else:
            thumbnail_customization_model = RobloxApiAvatarModelsAvatarThumbnailCustomizationModel.from_dict(
                _thumbnail_customization_model
            )

        error = d.pop("Error", UNSET)

        roblox_api_avatar_models_v4_response_invalid_thumbnail_customization_response = cls(
            thumbnail_customization_model=thumbnail_customization_model,
            error=error,
        )

        return roblox_api_avatar_models_v4_response_invalid_thumbnail_customization_response
