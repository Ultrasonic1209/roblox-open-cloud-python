from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiUpdateGroupNameResponse")


@_attrs_define
class RobloxGroupsApiUpdateGroupNameResponse:
    """
    Attributes:
        new_name (str | Unset): The new description returned
    """

    new_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_name = self.new_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if new_name is not UNSET:
            field_dict["newName"] = new_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        new_name = d.pop("newName", UNSET)

        roblox_groups_api_update_group_name_response = cls(
            new_name=new_name,
        )

        return roblox_groups_api_update_group_name_response
