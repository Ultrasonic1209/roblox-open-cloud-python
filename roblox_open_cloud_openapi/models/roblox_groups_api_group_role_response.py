from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_groups_api_group_role_response_color import RobloxGroupsApiGroupRoleResponseColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupRoleResponse")


@_attrs_define
class RobloxGroupsApiGroupRoleResponse:
    """A group role response model

    Attributes:
        id (int | Unset): The role id
        name (str | Unset): The role name
        description (str | Unset): The role description
        rank (int | Unset): The role rank
        member_count (int | Unset): The number of members in the role.
        is_base (bool | Unset): Whether or not the role is the base role for the group
        color (RobloxGroupsApiGroupRoleResponseColor | Unset): The role color. ['Invalid' = 0, 'Blue' = 1, 'Green' = 2,
            'Purple' = 3, 'Yellow' = 4, 'Orange' = 5, 'Red' = 6, 'Magenta' = 7, 'Teal' = 8, 'Turquoise' = 9, 'Rust' = 10,
            'Pistachio' = 11, 'Midnight' = 12, 'Lavender' = 13, 'Pink' = 14, 'Crimson' = 15, 'Plum' = 16]
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    rank: int | Unset = UNSET
    member_count: int | Unset = UNSET
    is_base: bool | Unset = UNSET
    color: RobloxGroupsApiGroupRoleResponseColor | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        rank = self.rank

        member_count = self.member_count

        is_base = self.is_base

        color: int | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if rank is not UNSET:
            field_dict["rank"] = rank
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if is_base is not UNSET:
            field_dict["isBase"] = is_base
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        rank = d.pop("rank", UNSET)

        member_count = d.pop("memberCount", UNSET)

        is_base = d.pop("isBase", UNSET)

        _color = d.pop("color", UNSET)
        color: RobloxGroupsApiGroupRoleResponseColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = RobloxGroupsApiGroupRoleResponseColor(_color)

        roblox_groups_api_group_role_response = cls(
            id=id,
            name=name,
            description=description,
            rank=rank,
            member_count=member_count,
            is_base=is_base,
            color=color,
        )

        return roblox_groups_api_group_role_response
