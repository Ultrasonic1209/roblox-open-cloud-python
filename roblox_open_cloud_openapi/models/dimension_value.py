from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DimensionValue")


@_attrs_define
class DimensionValue:
    """A single dimension value returned by a dimension values query.

    Attributes:
        value (str): The dimension value.
        display_value (None | str | Unset): A human-readable display value when the dimension is a unique ID.
    """

    value: str
    display_value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        display_value: None | str | Unset
        if isinstance(self.display_value, Unset):
            display_value = UNSET
        else:
            display_value = self.display_value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
            }
        )
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        value = d.pop("value")

        def _parse_display_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_value = _parse_display_value(d.pop("displayValue", UNSET))

        dimension_value = cls(
            value=value,
            display_value=display_value,
        )

        return dimension_value
