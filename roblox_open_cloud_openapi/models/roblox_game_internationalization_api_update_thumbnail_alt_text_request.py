from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiUpdateThumbnailAltTextRequest")


@_attrs_define
class RobloxGameInternationalizationApiUpdateThumbnailAltTextRequest:
    """
    Attributes:
        thumbnail_id (int | Unset):
        alt_text (str | Unset):
    """

    thumbnail_id: int | Unset = UNSET
    alt_text: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        thumbnail_id = self.thumbnail_id

        alt_text = self.alt_text

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if thumbnail_id is not UNSET:
            field_dict["thumbnailId"] = thumbnail_id
        if alt_text is not UNSET:
            field_dict["altText"] = alt_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thumbnail_id = d.pop("thumbnailId", UNSET)

        alt_text = d.pop("altText", UNSET)

        roblox_game_internationalization_api_update_thumbnail_alt_text_request = cls(
            thumbnail_id=thumbnail_id,
            alt_text=alt_text,
        )

        return roblox_game_internationalization_api_update_thumbnail_alt_text_request
