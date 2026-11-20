from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetStartPlaceOverrideEnabledRequestBody")


@_attrs_define
class SetStartPlaceOverrideEnabledRequestBody:
    """Request body for turning a universe's start place override on or off. The universe is
    identified by the route, so it is not part of the body.

        Attributes:
            enabled (bool | None | Unset): Whether game join routes players with the universe's start place override.
    """

    enabled: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        set_start_place_override_enabled_request_body = cls(
            enabled=enabled,
        )

        return set_start_place_override_enabled_request_body
