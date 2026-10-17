from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponseGameMediaItem")


@_attrs_define
class RobloxGamesApiModelsResponseGameMediaItem:
    """Response model for getting the game media item

    Attributes:
        id (int | Unset): The media item id.
        asset_type_id (int | Unset): The media item type id
        asset_type (str | Unset): The media item type, Image or YouTubeVideo
        image_id (int | Unset): The media item image id
        video_hash (str | Unset): The media item video hash
        video_title (str | Unset): The video title for video items.
        approved (bool | Unset): The media item is approved or not
        alt_text (str | Unset): The media item's alt text
    """

    id: int | Unset = UNSET
    asset_type_id: int | Unset = UNSET
    asset_type: str | Unset = UNSET
    image_id: int | Unset = UNSET
    video_hash: str | Unset = UNSET
    video_title: str | Unset = UNSET
    approved: bool | Unset = UNSET
    alt_text: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        asset_type_id = self.asset_type_id

        asset_type = self.asset_type

        image_id = self.image_id

        video_hash = self.video_hash

        video_title = self.video_title

        approved = self.approved

        alt_text = self.alt_text

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        asset_type_id = d.pop("assetTypeId", UNSET)

        asset_type = d.pop("assetType", UNSET)

        image_id = d.pop("imageId", UNSET)

        video_hash = d.pop("videoHash", UNSET)

        video_title = d.pop("videoTitle", UNSET)

        approved = d.pop("approved", UNSET)

        alt_text = d.pop("altText", UNSET)

        roblox_games_api_models_response_game_media_item = cls(
            id=id,
            asset_type_id=asset_type_id,
            asset_type=asset_type,
            image_id=image_id,
            video_hash=video_hash,
            video_title=video_title,
            approved=approved,
            alt_text=alt_text,
        )

        return roblox_games_api_models_response_game_media_item
