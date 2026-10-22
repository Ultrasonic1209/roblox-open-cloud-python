from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BreakdownFilter")


@_attrs_define
class BreakdownFilter:
    """Filter to apply when searching for the benchmark value.

    Attributes:
        dimension (str | Unset): The name of the dimension.
        value (str | Unset): The value of the dimension.
    """

    dimension: str | Unset = UNSET
    value: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dimension = d.pop("dimension", UNSET)

        value = d.pop("value", UNSET)

        breakdown_filter = cls(
            dimension=dimension,
            value=value,
        )

        return breakdown_filter
