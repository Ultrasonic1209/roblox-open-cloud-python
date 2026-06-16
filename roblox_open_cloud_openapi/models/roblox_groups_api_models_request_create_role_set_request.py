from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiModelsRequestCreateRoleSetRequest")


@_attrs_define
class RobloxGroupsApiModelsRequestCreateRoleSetRequest:
    """
    Attributes:
        name (str | Unset): The name of the roleset.
        description (str | Unset): The description of the roleset.
        rank (int | Unset): The rank/positioning of the roleset.
        using_group_funds (bool | Unset): Setting to use group funds or not.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    rank: int | Unset = UNSET
    using_group_funds: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        rank = self.rank

        using_group_funds = self.using_group_funds

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if rank is not UNSET:
            field_dict["rank"] = rank
        if using_group_funds is not UNSET:
            field_dict["usingGroupFunds"] = using_group_funds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        rank = d.pop("rank", UNSET)

        using_group_funds = d.pop("usingGroupFunds", UNSET)

        roblox_groups_api_models_request_create_role_set_request = cls(
            name=name,
            description=description,
            rank=rank,
            using_group_funds=using_group_funds,
        )

        return roblox_groups_api_models_request_create_role_set_request
