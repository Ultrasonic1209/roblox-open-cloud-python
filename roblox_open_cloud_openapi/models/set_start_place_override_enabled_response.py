from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetStartPlaceOverrideEnabledResponse")


@_attrs_define
class SetStartPlaceOverrideEnabledResponse:
    """Response for turning a universe's start place override on or off."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        set_start_place_override_enabled_response = cls()

        return set_start_place_override_enabled_response
