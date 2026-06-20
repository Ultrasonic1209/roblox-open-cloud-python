from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_web_responses_thumbnails_thumbnail_batch_response_state import (
    RobloxWebResponsesThumbnailsThumbnailBatchResponseState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesThumbnailsThumbnailBatchResponse")


@_attrs_define
class RobloxWebResponsesThumbnailsThumbnailBatchResponse:
    """
    Attributes:
        request_id (str | Unset):
        error_code (int | Unset):
        error_message (str | Unset):
        target_id (int | Unset):
        state (RobloxWebResponsesThumbnailsThumbnailBatchResponseState | Unset):  ['Error' = 0, 'Completed' = 1,
            'InReview' = 2, 'Pending' = 3, 'Blocked' = 4, 'TemporarilyUnavailable' = 5]
        image_url (str | Unset):
        version (str | Unset):
        thumbnail_source (str | Unset):
    """

    request_id: str | Unset = UNSET
    error_code: int | Unset = UNSET
    error_message: str | Unset = UNSET
    target_id: int | Unset = UNSET
    state: RobloxWebResponsesThumbnailsThumbnailBatchResponseState | Unset = UNSET
    image_url: str | Unset = UNSET
    version: str | Unset = UNSET
    thumbnail_source: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        error_code = self.error_code

        error_message = self.error_message

        target_id = self.target_id

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        image_url = self.image_url

        version = self.version

        thumbnail_source = self.thumbnail_source

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        request_id = d.pop("requestId", UNSET)

        error_code = d.pop("errorCode", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        target_id = d.pop("targetId", UNSET)

        _state = d.pop("state", UNSET)
        state: RobloxWebResponsesThumbnailsThumbnailBatchResponseState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RobloxWebResponsesThumbnailsThumbnailBatchResponseState(_state)

        image_url = d.pop("imageUrl", UNSET)

        version = d.pop("version", UNSET)

        thumbnail_source = d.pop("thumbnailSource", UNSET)

        roblox_web_responses_thumbnails_thumbnail_batch_response = cls(
            request_id=request_id,
            error_code=error_code,
            error_message=error_message,
            target_id=target_id,
            state=state,
            image_url=image_url,
            version=version,
            thumbnail_source=thumbnail_source,
        )

        return roblox_web_responses_thumbnails_thumbnail_batch_response
