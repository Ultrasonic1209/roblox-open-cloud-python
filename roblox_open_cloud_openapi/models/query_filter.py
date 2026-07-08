from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.filter_operation import FilterOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryFilter")


@_attrs_define
class QueryFilter:
    """A filter applied to a query dimension.

    Attributes:
        dimension (str): The dimension name to filter on.
        operation (FilterOperation): The operation to apply to a query filter.
        values (list[str] | Unset): The values to filter by.
    """

    dimension: str
    operation: FilterOperation
    values: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        operation = self.operation.value

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dimension": dimension,
                "operation": operation,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        dimension = d.pop("dimension")

        operation = FilterOperation(d.pop("operation"))

        values = cast(list[str], d.pop("values", UNSET))

        query_filter = cls(
            dimension=dimension,
            operation=operation,
            values=values,
        )

        return query_filter
