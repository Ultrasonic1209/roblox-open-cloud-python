from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardMetadataPatch")


@_attrs_define
class DashboardMetadataPatch:
    """DashboardMetadataPatch updates dashboard metadata without exposing storage rows.

    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        is_pinned (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_pinned: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_pinned: bool | None | Unset
        if isinstance(self.is_pinned, Unset):
            is_pinned = UNSET
        else:
            is_pinned = self.is_pinned

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_pinned is not UNSET:
            field_dict["isPinned"] = is_pinned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_pinned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_pinned = _parse_is_pinned(d.pop("isPinned", UNSET))

        dashboard_metadata_patch = cls(
            name=name,
            description=description,
            is_pinned=is_pinned,
        )

        return dashboard_metadata_patch
