from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BreakdownValue")


@_attrs_define
class BreakdownValue:
    """BreakdownValue the breakdown in the query result.

    Attributes:
        dimension (str | Unset): The name of the dimension.
        value (str | Unset): The value of the dimension.
        display_value (str | Unset): A display name for `value`. Not set in benchmark results.
    """

    dimension: str | Unset = UNSET
    value: str | Unset = UNSET
    display_value: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        value = self.value

        display_value = self.display_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if value is not UNSET:
            field_dict["value"] = value
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dimension = d.pop("dimension", UNSET)

        value = d.pop("value", UNSET)

        display_value = d.pop("displayValue", UNSET)

        breakdown_value = cls(
            dimension=dimension,
            value=value,
            display_value=display_value,
        )

        return breakdown_value
