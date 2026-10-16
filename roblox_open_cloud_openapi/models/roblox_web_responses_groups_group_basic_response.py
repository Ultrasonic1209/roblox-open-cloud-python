from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesGroupsGroupBasicResponse")


@_attrs_define
class RobloxWebResponsesGroupsGroupBasicResponse:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        member_count (int | Unset):
        has_verified_badge (bool | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    member_count: int | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        member_count = self.member_count

        has_verified_badge = self.has_verified_badge

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        member_count = d.pop("memberCount", UNSET)

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        roblox_web_responses_groups_group_basic_response = cls(
            id=id,
            name=name,
            member_count=member_count,
            has_verified_badge=has_verified_badge,
        )

        return roblox_web_responses_groups_group_basic_response
