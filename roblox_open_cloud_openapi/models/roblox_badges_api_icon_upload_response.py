from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxBadgesApiIconUploadResponse")


@_attrs_define
class RobloxBadgesApiIconUploadResponse:
    """Badge icon upload response.

    Attributes:
        target_id (int | Unset): The asset id of the uploaded icon.
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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        target_id = d.pop("targetId", UNSET)

        roblox_badges_api_icon_upload_response = cls(
            target_id=target_id,
        )

        return roblox_badges_api_icon_upload_response
