from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiUpdateGroupDescriptionRequest")


@_attrs_define
class RobloxGroupsApiUpdateGroupDescriptionRequest:
    """A request model for setting a description for the group

    Attributes:
        description (str | Unset): The group description being set.
    """

    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        description = d.pop("description", UNSET)

        roblox_groups_api_update_group_description_request = cls(
            description=description,
        )

        return roblox_groups_api_update_group_description_request
