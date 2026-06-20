from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesGamesGameMediaItemResponseV2")


@_attrs_define
class RobloxWebResponsesGamesGameMediaItemResponseV2:
    """Response model for getting the game media item

    Attributes:
        asset_type_id (int | Unset): The media item type id
        asset_type (str | Unset): The media item type, Image or YouTubeVideo
        image_id (int | Unset): The media item image id
        video_hash (str | Unset): The media item video hash
        video_title (str | Unset): The video title for video items.
        approved (bool | Unset): The media item is approved or not
        alt_text (str | Unset): The media item alt text
        video_id (str | Unset): The video asset ID
    """

    asset_type_id: int | Unset = UNSET
    asset_type: str | Unset = UNSET
    image_id: int | Unset = UNSET
    video_hash: str | Unset = UNSET
    video_title: str | Unset = UNSET
    approved: bool | Unset = UNSET
    alt_text: str | Unset = UNSET
    video_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_type_id = self.asset_type_id

        asset_type = self.asset_type

        image_id = self.image_id

        video_hash = self.video_hash

        video_title = self.video_title

        approved = self.approved

        alt_text = self.alt_text

        video_id = self.video_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_type_id is not UNSET:
            field_dict["assetTypeId"] = asset_type_id
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if video_hash is not UNSET:
            field_dict["videoHash"] = video_hash
        if video_title is not UNSET:
            field_dict["videoTitle"] = video_title
        if approved is not UNSET:
            field_dict["approved"] = approved
        if alt_text is not UNSET:
            field_dict["altText"] = alt_text
        if video_id is not UNSET:
            field_dict["videoId"] = video_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_type_id = d.pop("assetTypeId", UNSET)

        asset_type = d.pop("assetType", UNSET)

        image_id = d.pop("imageId", UNSET)

        video_hash = d.pop("videoHash", UNSET)

        video_title = d.pop("videoTitle", UNSET)

        approved = d.pop("approved", UNSET)

        alt_text = d.pop("altText", UNSET)

        video_id = d.pop("videoId", UNSET)

        roblox_web_responses_games_game_media_item_response_v2 = cls(
            asset_type_id=asset_type_id,
            asset_type=asset_type,
            image_id=image_id,
            video_hash=video_hash,
            video_title=video_title,
            approved=approved,
            alt_text=alt_text,
            video_id=video_id,
        )

        return roblox_web_responses_games_game_media_item_response_v2
