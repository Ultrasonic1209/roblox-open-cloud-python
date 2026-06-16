from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupDescriptionResponse")


@_attrs_define
class RobloxGroupsApiGroupDescriptionResponse:
    """
    Attributes:
        new_description (str | Unset): The new description returned
    """

    new_description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_description = self.new_description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if new_description is not UNSET:
            field_dict["newDescription"] = new_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_description = d.pop("newDescription", UNSET)

        roblox_groups_api_group_description_response = cls(
            new_description=new_description,
        )

        return roblox_groups_api_group_description_response
