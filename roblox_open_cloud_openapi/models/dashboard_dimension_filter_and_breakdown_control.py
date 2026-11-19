from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_unfiltered_entry import DashboardUnfilteredEntry


T = TypeVar("T", bound="DashboardDimensionFilterAndBreakdownControl")


@_attrs_define
class DashboardDimensionFilterAndBreakdownControl:
    """DashboardDimensionFilterAndBreakdownControl defines one local dimension filter and breakdown control.

    Attributes:
        filter_dimension_key (None | str | Unset):  Default: ''.
        breakdown_dimension_keys (list[str] | None | Unset):
        default_filter_dimension_value (None | str | Unset):  Default: ''.
        unfiltered_entry (DashboardUnfilteredEntry | None | Unset): DashboardUnfilteredEntry defines the unfiltered
            selector option for a dimension control.
    """

    filter_dimension_key: None | str | Unset = ""
    breakdown_dimension_keys: list[str] | None | Unset = UNSET
    default_filter_dimension_value: None | str | Unset = ""
    unfiltered_entry: DashboardUnfilteredEntry | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_unfiltered_entry import DashboardUnfilteredEntry  # noqa: PLC0415

        filter_dimension_key: None | str | Unset
        if isinstance(self.filter_dimension_key, Unset):
            filter_dimension_key = UNSET
        else:
            filter_dimension_key = self.filter_dimension_key

        breakdown_dimension_keys: list[str] | None | Unset
        if isinstance(self.breakdown_dimension_keys, Unset):
            breakdown_dimension_keys = UNSET
        elif isinstance(self.breakdown_dimension_keys, list):
            breakdown_dimension_keys = self.breakdown_dimension_keys

        else:
            breakdown_dimension_keys = self.breakdown_dimension_keys

        default_filter_dimension_value: None | str | Unset
        if isinstance(self.default_filter_dimension_value, Unset):
            default_filter_dimension_value = UNSET
        else:
            default_filter_dimension_value = self.default_filter_dimension_value

        unfiltered_entry: dict[str, Any] | None | Unset
        if isinstance(self.unfiltered_entry, Unset):
            unfiltered_entry = UNSET
        elif isinstance(self.unfiltered_entry, DashboardUnfilteredEntry):
            unfiltered_entry = self.unfiltered_entry.to_dict()
        else:
            unfiltered_entry = self.unfiltered_entry

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filter_dimension_key is not UNSET:
            field_dict["filterDimensionKey"] = filter_dimension_key
        if breakdown_dimension_keys is not UNSET:
            field_dict["breakdownDimensionKeys"] = breakdown_dimension_keys
        if default_filter_dimension_value is not UNSET:
            field_dict["defaultFilterDimensionValue"] = default_filter_dimension_value
        if unfiltered_entry is not UNSET:
            field_dict["unfilteredEntry"] = unfiltered_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_unfiltered_entry import DashboardUnfilteredEntry  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_filter_dimension_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_dimension_key = _parse_filter_dimension_key(d.pop("filterDimensionKey", UNSET))

        def _parse_breakdown_dimension_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breakdown_dimension_keys_type_0 = cast(list[str], data)

                return breakdown_dimension_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        breakdown_dimension_keys = _parse_breakdown_dimension_keys(d.pop("breakdownDimensionKeys", UNSET))

        def _parse_default_filter_dimension_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_filter_dimension_value = _parse_default_filter_dimension_value(
            d.pop("defaultFilterDimensionValue", UNSET)
        )

        def _parse_unfiltered_entry(data: object) -> DashboardUnfilteredEntry | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unfiltered_entry_type_0 = DashboardUnfilteredEntry.from_dict(data)

                return unfiltered_entry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardUnfilteredEntry | None | Unset, data)

        unfiltered_entry = _parse_unfiltered_entry(d.pop("unfilteredEntry", UNSET))

        dashboard_dimension_filter_and_breakdown_control = cls(
            filter_dimension_key=filter_dimension_key,
            breakdown_dimension_keys=breakdown_dimension_keys,
            default_filter_dimension_value=default_filter_dimension_value,
            unfiltered_entry=unfiltered_entry,
        )

        return dashboard_dimension_filter_and_breakdown_control
