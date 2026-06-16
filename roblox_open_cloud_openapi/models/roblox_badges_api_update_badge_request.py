from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxBadgesApiUpdateBadgeRequest")


@_attrs_define
class RobloxBadgesApiUpdateBadgeRequest:
    """A request model used for updating badge information.

    Attributes:
        name (str | Unset): The new badge name.
        description (str | Unset): The new badge description.
        enabled (bool | Unset): The new enabled state of the badge.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        roblox_badges_api_update_badge_request = cls(
            name=name,
            description=description,
            enabled=enabled,
        )

        return roblox_badges_api_update_badge_request
