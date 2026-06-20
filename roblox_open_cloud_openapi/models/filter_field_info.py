from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.filter_field import FilterField
from ..models.filter_type import FilterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterFieldInfo")


@_attrs_define
class FilterFieldInfo:
    """Describes the metadata and available values for a single filter field.

    Attributes:
        field (FilterField | Unset): Enum describing the different available filter fields.
        type_ (FilterType | Unset): Enum describing the data type of a filter field's values.
        values (list[Any] | None | Unset): The list of available values for the filter.
    """

    field: FilterField | Unset = UNSET
    type_: FilterType | Unset = UNSET
    values: list[Any] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field: str | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        values: list[Any] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = self.values

        else:
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if type_ is not UNSET:
            field_dict["type"] = type_
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _field = d.pop("field", UNSET)
        field: FilterField | Unset
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = FilterField(_field)

        _type_ = d.pop("type", UNSET)
        type_: FilterType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FilterType(_type_)

        def _parse_values(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[Any], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))

        filter_field_info = cls(
            field=field,
            type_=type_,
            values=values,
        )

        return filter_field_info
