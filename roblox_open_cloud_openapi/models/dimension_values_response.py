from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimension_values import DimensionValues


T = TypeVar("T", bound="DimensionValuesResponse")


@_attrs_define
class DimensionValuesResponse:
    """The response for a dimension values query.

    Attributes:
        values (list[DimensionValues] | Unset): The dimension values returned by the query.
    """

    values: list[DimensionValues] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_values import DimensionValues

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _values = d.pop("values", UNSET)
        values: list[DimensionValues] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = DimensionValues.from_dict(values_item_data)

                values.append(values_item)

        dimension_values_response = cls(
            values=values,
        )

        return dimension_values_response
