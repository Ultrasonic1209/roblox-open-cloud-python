from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsClientGroupFeaturedContentResponse")


@_attrs_define
class RobloxGroupsClientGroupFeaturedContentResponse:
    """
    Attributes:
        group_id (int | Unset):
        content_type (str | Unset):
        content_id (str | Unset):
    """

    group_id: int | Unset = UNSET
    content_type: str | Unset = UNSET
    content_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        content_type = self.content_type

        content_id = self.content_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if content_id is not UNSET:
            field_dict["contentId"] = content_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        group_id = d.pop("groupId", UNSET)

        content_type = d.pop("contentType", UNSET)

        content_id = d.pop("contentId", UNSET)

        roblox_groups_client_group_featured_content_response = cls(
            group_id=group_id,
            content_type=content_type,
            content_id=content_id,
        )

        return roblox_groups_client_group_featured_content_response
