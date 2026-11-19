from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_custom_date_range import DashboardCustomDateRange


T = TypeVar("T", bound="DashboardDateRangeDefault")


@_attrs_define
class DashboardDateRangeDefault:
    """DashboardDateRangeDefault selects the initial date range for a surface.

    Attributes:
        relative_range_key (None | str | Unset):
        custom_range (DashboardCustomDateRange | None | Unset): DashboardCustomDateRange stores an explicit start and
            end time.
    """

    relative_range_key: None | str | Unset = UNSET
    custom_range: DashboardCustomDateRange | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_custom_date_range import DashboardCustomDateRange  # noqa: PLC0415

        relative_range_key: None | str | Unset
        if isinstance(self.relative_range_key, Unset):
            relative_range_key = UNSET
        else:
            relative_range_key = self.relative_range_key

        custom_range: dict[str, Any] | None | Unset
        if isinstance(self.custom_range, Unset):
            custom_range = UNSET
        elif isinstance(self.custom_range, DashboardCustomDateRange):
            custom_range = self.custom_range.to_dict()
        else:
            custom_range = self.custom_range

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if relative_range_key is not UNSET:
            field_dict["relativeRangeKey"] = relative_range_key
        if custom_range is not UNSET:
            field_dict["customRange"] = custom_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_custom_date_range import DashboardCustomDateRange  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_relative_range_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relative_range_key = _parse_relative_range_key(d.pop("relativeRangeKey", UNSET))

        def _parse_custom_range(data: object) -> DashboardCustomDateRange | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_range_type_0 = DashboardCustomDateRange.from_dict(data)

                return custom_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardCustomDateRange | None | Unset, data)

        custom_range = _parse_custom_range(d.pop("customRange", UNSET))

        dashboard_date_range_default = cls(
            relative_range_key=relative_range_key,
            custom_range=custom_range,
        )

        return dashboard_date_range_default
