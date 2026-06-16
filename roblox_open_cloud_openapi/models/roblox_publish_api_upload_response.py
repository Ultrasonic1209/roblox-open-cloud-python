from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPublishApiUploadResponse")


@_attrs_define
class RobloxPublishApiUploadResponse:
    """A response used when an upload has completed.

    Attributes:
        target_id (int | Unset): The target Id of the uploaded item.
    """

    target_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_id = self.target_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_id is not UNSET:
            field_dict["targetId"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_id = d.pop("targetId", UNSET)

        roblox_publish_api_upload_response = cls(
            target_id=target_id,
        )

        return roblox_publish_api_upload_response
