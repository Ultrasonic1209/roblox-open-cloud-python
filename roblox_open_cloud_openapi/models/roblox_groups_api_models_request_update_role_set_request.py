from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiModelsRequestUpdateRoleSetRequest")


@_attrs_define
class RobloxGroupsApiModelsRequestUpdateRoleSetRequest:
    """
    Attributes:
        name (str | Unset): The name of the roleset.
        description (str | Unset): The description of the roleset.
        rank (int | Unset): The rank/positioning of the roleset.
        color (int | Unset): Optional. The color of the roleset (GroupRoleSetColorType value, e.g. 0 = Invalid, 1 =
            Blue).
            When omitted, only name and description are updated and the existing color is left unchanged.
            When set, name, description, and color are updated via UpdateGroupRoleSetProperties.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    rank: int | Unset = UNSET
    color: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        rank = self.rank

        color = self.color

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if rank is not UNSET:
            field_dict["rank"] = rank
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        rank = d.pop("rank", UNSET)

        color = d.pop("color", UNSET)

        roblox_groups_api_models_request_update_role_set_request = cls(
            name=name,
            description=description,
            rank=rank,
            color=color,
        )

        return roblox_groups_api_models_request_update_role_set_request
