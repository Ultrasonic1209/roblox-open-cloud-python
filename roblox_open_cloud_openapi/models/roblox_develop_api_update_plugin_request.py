from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxDevelopApiUpdatePluginRequest")


@_attrs_define
class RobloxDevelopApiUpdatePluginRequest:
    """A request model for updating a plugin.

    Attributes:
        name (str | Unset): The new plugin name.
        description (str | Unset): The new plugin description.
        comments_enabled (bool | Unset): Whether or not comments should be enabled.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    comments_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        comments_enabled = self.comments_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if comments_enabled is not UNSET:
            field_dict["commentsEnabled"] = comments_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        comments_enabled = d.pop("commentsEnabled", UNSET)

        roblox_develop_api_update_plugin_request = cls(
            name=name,
            description=description,
            comments_enabled=comments_enabled,
        )

        return roblox_develop_api_update_plugin_request
