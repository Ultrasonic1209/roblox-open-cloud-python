from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse")


@_attrs_define
class RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse:
    """
    Attributes:
        media_asset_id (str | Unset):
    """

    media_asset_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        media_asset_id = self.media_asset_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if media_asset_id is not UNSET:
            field_dict["mediaAssetId"] = media_asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        media_asset_id = d.pop("mediaAssetId", UNSET)

        roblox_game_internationalization_api_models_response_upload_image_for_game_thumbnail_response = cls(
            media_asset_id=media_asset_id,
        )

        return roblox_game_internationalization_api_models_response_upload_image_for_game_thumbnail_response
