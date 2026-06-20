from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiMembersRequest")


@_attrs_define
class RobloxGroupsApiMembersRequest:
    """
    Attributes:
        user_ids (list[int] | Unset): The user ids being either accepted or declined
    """

    user_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_ids: list[int] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_ids is not UNSET:
            field_dict["UserIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_ids = cast(list[int], d.pop("UserIds", UNSET))

        roblox_groups_api_members_request = cls(
            user_ids=user_ids,
        )

        return roblox_groups_api_members_request
