from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimension_value import DimensionValue


T = TypeVar("T", bound="DimensionValues")


@_attrs_define
class DimensionValues:
    """The values for a single dimension returned by a dimension values query.

    Attributes:
        dimension (str): The dimension name.
        values (list[DimensionValue] | Unset): The values for the dimension.
    """

    dimension: str
    values: list[DimensionValue] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dimension": dimension,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension_value import DimensionValue

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        dimension = d.pop("dimension")

        _values = d.pop("values", UNSET)
        values: list[DimensionValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = DimensionValue.from_dict(values_item_data)

                values.append(values_item)

        dimension_values = cls(
            dimension=dimension,
            values=values,
        )

        return dimension_values
