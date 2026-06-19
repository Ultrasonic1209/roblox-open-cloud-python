from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.thumbnails_api_roblox_web_responses_thumbnails_thumbnail_response_state import (
    ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponseState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse")


@_attrs_define
class ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse:
    """
    Attributes:
        target_id (int | Unset):
        state (ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponseState | Unset):  ['Error' = 0, 'Completed' = 1,
            'InReview' = 2, 'Pending' = 3, 'Blocked' = 4, 'TemporarilyUnavailable' = 5]
        image_url (str | Unset):
        version (str | Unset):
        thumbnail_source (str | Unset):
    """

    target_id: int | Unset = UNSET
    state: ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponseState | Unset = UNSET
    image_url: str | Unset = UNSET
    version: str | Unset = UNSET
    thumbnail_source: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        image_url = self.image_url

        version = self.version

        thumbnail_source = self.thumbnail_source

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if state is not UNSET:
            field_dict["state"] = state
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if version is not UNSET:
            field_dict["version"] = version
        if thumbnail_source is not UNSET:
            field_dict["thumbnailSource"] = thumbnail_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_id = d.pop("targetId", UNSET)

        _state = d.pop("state", UNSET)
        state: ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponseState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponseState(_state)

        image_url = d.pop("imageUrl", UNSET)

        version = d.pop("version", UNSET)

        thumbnail_source = d.pop("thumbnailSource", UNSET)

        thumbnails_api_roblox_web_responses_thumbnails_thumbnail_response = cls(
            target_id=target_id,
            state=state,
            image_url=image_url,
            version=version,
            thumbnail_source=thumbnail_source,
        )

        return thumbnails_api_roblox_web_responses_thumbnails_thumbnail_response
