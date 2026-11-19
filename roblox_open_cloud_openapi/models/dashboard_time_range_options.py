from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_date_range_options import DashboardDateRangeOptions
    from ..models.dashboard_no_time_range_options import DashboardNoTimeRangeOptions


T = TypeVar("T", bound="DashboardTimeRangeOptions")


@_attrs_define
class DashboardTimeRangeOptions:
    """DashboardTimeRangeOptions defines the available time range behavior for a surface.

    Attributes:
        none (DashboardNoTimeRangeOptions | None | Unset): DashboardNoTimeRangeOptions disables time range controls for
            a surface.
        date_range (DashboardDateRangeOptions | None | Unset): DashboardDateRangeOptions defines date range control
            behavior for a surface.
    """

    none: DashboardNoTimeRangeOptions | None | Unset = UNSET
    date_range: DashboardDateRangeOptions | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_date_range_options import DashboardDateRangeOptions  # noqa: PLC0415
        from ..models.dashboard_no_time_range_options import DashboardNoTimeRangeOptions  # noqa: PLC0415

        none: dict[str, Any] | None | Unset
        if isinstance(self.none, Unset):
            none = UNSET
        elif isinstance(self.none, DashboardNoTimeRangeOptions):
            none = self.none.to_dict()
        else:
            none = self.none

        date_range: dict[str, Any] | None | Unset
        if isinstance(self.date_range, Unset):
            date_range = UNSET
        elif isinstance(self.date_range, DashboardDateRangeOptions):
            date_range = self.date_range.to_dict()
        else:
            date_range = self.date_range

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if none is not UNSET:
            field_dict["none"] = none
        if date_range is not UNSET:
            field_dict["dateRange"] = date_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_date_range_options import DashboardDateRangeOptions  # noqa: PLC0415
        from ..models.dashboard_no_time_range_options import DashboardNoTimeRangeOptions  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_none(data: object) -> DashboardNoTimeRangeOptions | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                none_type_0 = DashboardNoTimeRangeOptions.from_dict(data)

                return none_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardNoTimeRangeOptions | None | Unset, data)

        none = _parse_none(d.pop("none", UNSET))

        def _parse_date_range(data: object) -> DashboardDateRangeOptions | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                date_range_type_0 = DashboardDateRangeOptions.from_dict(data)

                return date_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardDateRangeOptions | None | Unset, data)

        date_range = _parse_date_range(d.pop("dateRange", UNSET))

        dashboard_time_range_options = cls(
            none=none,
            date_range=date_range,
        )

        return dashboard_time_range_options
