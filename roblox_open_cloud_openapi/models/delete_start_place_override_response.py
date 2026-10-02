from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DeleteStartPlaceOverrideResponse")


@_attrs_define
class DeleteStartPlaceOverrideResponse:
    """Response for deleting the start place override for a universe."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        delete_start_place_override_response = cls()

        return delete_start_place_override_response
