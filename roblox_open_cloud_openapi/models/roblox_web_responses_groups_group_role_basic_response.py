from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesGroupsGroupRoleBasicResponse")


@_attrs_define
class RobloxWebResponsesGroupsGroupRoleBasicResponse:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        rank (int | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    rank: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        rank = self.rank

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rank = d.pop("rank", UNSET)

        roblox_web_responses_groups_group_role_basic_response = cls(
            id=id,
            name=name,
            rank=rank,
        )

        return roblox_web_responses_groups_group_role_basic_response
