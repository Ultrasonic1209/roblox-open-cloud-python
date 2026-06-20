from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiRelationshipsRequest")


@_attrs_define
class RobloxGroupsApiRelationshipsRequest:
    """
    Attributes:
        group_ids (list[int] | Unset): The group ids being either accepted or declined
    """

    group_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_ids: list[int] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_ids is not UNSET:
            field_dict["GroupIds"] = group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        group_ids = cast(list[int], d.pop("GroupIds", UNSET))

        roblox_groups_api_relationships_request = cls(
            group_ids=group_ids,
        )

        return roblox_groups_api_relationships_request
