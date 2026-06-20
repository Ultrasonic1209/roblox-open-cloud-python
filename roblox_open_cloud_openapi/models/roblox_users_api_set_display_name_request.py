from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiSetDisplayNameRequest")


@_attrs_define
class RobloxUsersApiSetDisplayNameRequest:
    """Request model for changing a display name.

    Attributes:
        new_display_name (str | Unset): The users new display name.
    """

    new_display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_display_name = self.new_display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if new_display_name is not UNSET:
            field_dict["newDisplayName"] = new_display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        new_display_name = d.pop("newDisplayName", UNSET)

        roblox_users_api_set_display_name_request = cls(
            new_display_name=new_display_name,
        )

        return roblox_users_api_set_display_name_request
