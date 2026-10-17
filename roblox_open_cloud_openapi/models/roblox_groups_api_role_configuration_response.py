from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiRoleConfigurationResponse")


@_attrs_define
class RobloxGroupsApiRoleConfigurationResponse:
    """A response model for role configuration

    Attributes:
        name_max_length (int | Unset): The maximum length of a role name
        description_max_length (int | Unset): The maximum length of a role description
        limit (int | Unset): The maximum number of roles in a group
        cost (int | Unset): The cost of purchasing a role
        min_rank (int | Unset): The minimum rank a role can have
        max_rank (int | Unset): The maximum rank a role can have
    """

    name_max_length: int | Unset = UNSET
    description_max_length: int | Unset = UNSET
    limit: int | Unset = UNSET
    cost: int | Unset = UNSET
    min_rank: int | Unset = UNSET
    max_rank: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name_max_length = self.name_max_length

        description_max_length = self.description_max_length

        limit = self.limit

        cost = self.cost

        min_rank = self.min_rank

        max_rank = self.max_rank

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name_max_length is not UNSET:
            field_dict["nameMaxLength"] = name_max_length
        if description_max_length is not UNSET:
            field_dict["descriptionMaxLength"] = description_max_length
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cost is not UNSET:
            field_dict["cost"] = cost
        if min_rank is not UNSET:
            field_dict["minRank"] = min_rank
        if max_rank is not UNSET:
            field_dict["maxRank"] = max_rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name_max_length = d.pop("nameMaxLength", UNSET)

        description_max_length = d.pop("descriptionMaxLength", UNSET)

        limit = d.pop("limit", UNSET)

        cost = d.pop("cost", UNSET)

        min_rank = d.pop("minRank", UNSET)

        max_rank = d.pop("maxRank", UNSET)

        roblox_groups_api_role_configuration_response = cls(
            name_max_length=name_max_length,
            description_max_length=description_max_length,
            limit=limit,
            cost=cost,
            min_rank=min_rank,
            max_rank=max_rank,
        )

        return roblox_groups_api_role_configuration_response
