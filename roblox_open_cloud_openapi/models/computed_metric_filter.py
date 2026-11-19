from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputedMetricFilter")


@_attrs_define
class ComputedMetricFilter:
    """ComputedMetricFilter is an authoring-time source filter. Keep this message
    wire-compatible with TileFilter for schema-v1 computed sources.

        Attributes:
            dimension_key (None | str | Unset):  Default: ''.
            values (list[str] | None | Unset):
    """

    dimension_key: None | str | Unset = ""
    values: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dimension_key: None | str | Unset
        if isinstance(self.dimension_key, Unset):
            dimension_key = UNSET
        else:
            dimension_key = self.dimension_key

        values: list[str] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = self.values

        else:
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dimension_key is not UNSET:
            field_dict["dimensionKey"] = dimension_key
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_dimension_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dimension_key = _parse_dimension_key(d.pop("dimensionKey", UNSET))

        def _parse_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[str], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))

        computed_metric_filter = cls(
            dimension_key=dimension_key,
            values=values,
        )

        return computed_metric_filter
