from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dashboard_time_range_subcontext_control_mode_type_0_type_0 import (
    DashboardTimeRangeSubcontextControlModeType0Type0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_time_range_subcontext_granularity_by_date_range_type_0 import (
        DashboardTimeRangeSubcontextGranularityByDateRangeType0,
    )


T = TypeVar("T", bound="DashboardTimeRangeSubcontext")


@_attrs_define
class DashboardTimeRangeSubcontext:
    """DashboardTimeRangeSubcontext applies a local time range control to a component.

    Attributes:
        control_mode (DashboardTimeRangeSubcontextControlModeType0Type0 | int | None | Unset):
            DashboardTimeRangeControlMode describes how time range controls are exposed. Default:
            DashboardTimeRangeSubcontextControlModeType0Type0.DASHBOARD_TIME_RANGE_CONTROL_MODE_INVALID.
        date_range_keys (list[str] | None | Unset):
        default_date_range_key (None | str | Unset):  Default: ''.
        granularity_by_date_range (DashboardTimeRangeSubcontextGranularityByDateRangeType0 | None | Unset):
    """

    control_mode: DashboardTimeRangeSubcontextControlModeType0Type0 | int | None | Unset = (
        DashboardTimeRangeSubcontextControlModeType0Type0.DASHBOARD_TIME_RANGE_CONTROL_MODE_INVALID
    )
    date_range_keys: list[str] | None | Unset = UNSET
    default_date_range_key: None | str | Unset = ""
    granularity_by_date_range: DashboardTimeRangeSubcontextGranularityByDateRangeType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_time_range_subcontext_granularity_by_date_range_type_0 import (
            DashboardTimeRangeSubcontextGranularityByDateRangeType0,  # noqa: PLC0415
        )

        control_mode: int | None | str | Unset
        if isinstance(self.control_mode, Unset):
            control_mode = UNSET
        elif isinstance(self.control_mode, DashboardTimeRangeSubcontextControlModeType0Type0):
            control_mode = self.control_mode.value
        else:
            control_mode = self.control_mode

        date_range_keys: list[str] | None | Unset
        if isinstance(self.date_range_keys, Unset):
            date_range_keys = UNSET
        elif isinstance(self.date_range_keys, list):
            date_range_keys = self.date_range_keys

        else:
            date_range_keys = self.date_range_keys

        default_date_range_key: None | str | Unset
        if isinstance(self.default_date_range_key, Unset):
            default_date_range_key = UNSET
        else:
            default_date_range_key = self.default_date_range_key

        granularity_by_date_range: dict[str, Any] | None | Unset
        if isinstance(self.granularity_by_date_range, Unset):
            granularity_by_date_range = UNSET
        elif isinstance(self.granularity_by_date_range, DashboardTimeRangeSubcontextGranularityByDateRangeType0):
            granularity_by_date_range = self.granularity_by_date_range.to_dict()
        else:
            granularity_by_date_range = self.granularity_by_date_range

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if control_mode is not UNSET:
            field_dict["controlMode"] = control_mode
        if date_range_keys is not UNSET:
            field_dict["dateRangeKeys"] = date_range_keys
        if default_date_range_key is not UNSET:
            field_dict["defaultDateRangeKey"] = default_date_range_key
        if granularity_by_date_range is not UNSET:
            field_dict["granularityByDateRange"] = granularity_by_date_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_time_range_subcontext_granularity_by_date_range_type_0 import (
            DashboardTimeRangeSubcontextGranularityByDateRangeType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_control_mode(data: object) -> DashboardTimeRangeSubcontextControlModeType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                control_mode_type_0_type_0 = DashboardTimeRangeSubcontextControlModeType0Type0(data)

                return control_mode_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardTimeRangeSubcontextControlModeType0Type0 | int | None | Unset, data)

        control_mode = _parse_control_mode(d.pop("controlMode", UNSET))

        def _parse_date_range_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                date_range_keys_type_0 = cast(list[str], data)

                return date_range_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        date_range_keys = _parse_date_range_keys(d.pop("dateRangeKeys", UNSET))

        def _parse_default_date_range_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_date_range_key = _parse_default_date_range_key(d.pop("defaultDateRangeKey", UNSET))

        def _parse_granularity_by_date_range(
            data: object,
        ) -> DashboardTimeRangeSubcontextGranularityByDateRangeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                granularity_by_date_range_type_0 = DashboardTimeRangeSubcontextGranularityByDateRangeType0.from_dict(
                    data
                )

                return granularity_by_date_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardTimeRangeSubcontextGranularityByDateRangeType0 | None | Unset, data)

        granularity_by_date_range = _parse_granularity_by_date_range(d.pop("granularityByDateRange", UNSET))

        dashboard_time_range_subcontext = cls(
            control_mode=control_mode,
            date_range_keys=date_range_keys,
            default_date_range_key=default_date_range_key,
            granularity_by_date_range=granularity_by_date_range,
        )

        return dashboard_time_range_subcontext
