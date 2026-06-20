from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiSortImageIdsRequest")


@_attrs_define
class RobloxGameInternationalizationApiSortImageIdsRequest:
    """A request model for sorting of image Ids for game thumbnails

    Attributes:
        media_asset_ids (list[int] | Unset): List of thumbnail ids in desired order.
    """

    media_asset_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        media_asset_ids: list[int] | Unset = UNSET
        if not isinstance(self.media_asset_ids, Unset):
            media_asset_ids = self.media_asset_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if media_asset_ids is not UNSET:
            field_dict["mediaAssetIds"] = media_asset_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        media_asset_ids = cast(list[int], d.pop("mediaAssetIds", UNSET))

        roblox_game_internationalization_api_sort_image_ids_request = cls(
            media_asset_ids=media_asset_ids,
        )

        return roblox_game_internationalization_api_sort_image_ids_request
