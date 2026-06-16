from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiPostGroupStatusRequest")


@_attrs_define
class RobloxGroupsApiPostGroupStatusRequest:
    """A request model for setting the authenticated user's primary group.

    Attributes:
        message (str | Unset): The message to set the group status to.
    """

    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        roblox_groups_api_post_group_status_request = cls(
            message=message,
        )

        return roblox_groups_api_post_group_status_request
