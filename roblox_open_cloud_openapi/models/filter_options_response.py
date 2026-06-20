from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_options_response_filters_type_0 import FilterOptionsResponseFiltersType0


T = TypeVar("T", bound="FilterOptionsResponse")


@_attrs_define
class FilterOptionsResponse:
    """Response model for filter options endpoint.

    Attributes:
        filters (FilterOptionsResponseFiltersType0 | None | Unset): A dictionary of filter field names to their metadata
            and available values.
    """

    filters: FilterOptionsResponseFiltersType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_options_response_filters_type_0 import FilterOptionsResponseFiltersType0

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, FilterOptionsResponseFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_options_response_filters_type_0 import FilterOptionsResponseFiltersType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_filters(data: object) -> FilterOptionsResponseFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = FilterOptionsResponseFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FilterOptionsResponseFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        filter_options_response = cls(
            filters=filters,
        )

        return filter_options_response
