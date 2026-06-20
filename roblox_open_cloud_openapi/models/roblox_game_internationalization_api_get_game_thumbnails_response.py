from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_media_asset_response import (
        RobloxGameInternationalizationApiMediaAssetResponse,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiGetGameThumbnailsResponse")


@_attrs_define
class RobloxGameInternationalizationApiGetGameThumbnailsResponse:
    """
    Attributes:
        language_code (str | Unset):
        media_assets (list[RobloxGameInternationalizationApiMediaAssetResponse] | Unset):
    """

    language_code: str | Unset = UNSET
    media_assets: list[RobloxGameInternationalizationApiMediaAssetResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        language_code = self.language_code

        media_assets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.media_assets, Unset):
            media_assets = []
            for media_assets_item_data in self.media_assets:
                media_assets_item = media_assets_item_data.to_dict()
                media_assets.append(media_assets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if media_assets is not UNSET:
            field_dict["mediaAssets"] = media_assets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_media_asset_response import (
            RobloxGameInternationalizationApiMediaAssetResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        language_code = d.pop("languageCode", UNSET)

        _media_assets = d.pop("mediaAssets", UNSET)
        media_assets: list[RobloxGameInternationalizationApiMediaAssetResponse] | Unset = UNSET
        if _media_assets is not UNSET:
            media_assets = []
            for media_assets_item_data in _media_assets:
                media_assets_item = RobloxGameInternationalizationApiMediaAssetResponse.from_dict(
                    media_assets_item_data
                )

                media_assets.append(media_assets_item)

        roblox_game_internationalization_api_get_game_thumbnails_response = cls(
            language_code=language_code,
            media_assets=media_assets,
        )

        return roblox_game_internationalization_api_get_game_thumbnails_response
