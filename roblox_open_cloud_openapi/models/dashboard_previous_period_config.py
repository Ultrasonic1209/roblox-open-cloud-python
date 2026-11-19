from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dashboard_previous_period_config_relative_offset_type_0_type_0 import (
    DashboardPreviousPeriodConfigRelativeOffsetType0Type0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardPreviousPeriodConfig")


@_attrs_define
class DashboardPreviousPeriodConfig:
    """DashboardPreviousPeriodConfig stores an authored previous-period comparison.
    relative_offset and custom_start_time are optional independently so the
    contract can losslessly preserve Creator Hub editor state.

        Attributes:
            relative_offset (DashboardPreviousPeriodConfigRelativeOffsetType0Type0 | int | None | Unset):
                DashboardComparisonRelativeOffset selects a fixed lookback for a configured
                previous-period comparison. Default:
                DashboardPreviousPeriodConfigRelativeOffsetType0Type0.DASHBOARD_COMPARISON_RELATIVE_OFFSET_INVALID.
            custom_start_time (datetime.datetime | None | Unset):
    """

    relative_offset: DashboardPreviousPeriodConfigRelativeOffsetType0Type0 | int | None | Unset = (
        DashboardPreviousPeriodConfigRelativeOffsetType0Type0.DASHBOARD_COMPARISON_RELATIVE_OFFSET_INVALID
    )
    custom_start_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        relative_offset: int | None | str | Unset
        if isinstance(self.relative_offset, Unset):
            relative_offset = UNSET
        elif isinstance(self.relative_offset, DashboardPreviousPeriodConfigRelativeOffsetType0Type0):
            relative_offset = self.relative_offset.value
        else:
            relative_offset = self.relative_offset

        custom_start_time: None | str | Unset
        if isinstance(self.custom_start_time, Unset):
            custom_start_time = UNSET
        elif isinstance(self.custom_start_time, datetime.datetime):
            custom_start_time = self.custom_start_time.isoformat()
        else:
            custom_start_time = self.custom_start_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if relative_offset is not UNSET:
            field_dict["relativeOffset"] = relative_offset
        if custom_start_time is not UNSET:
            field_dict["customStartTime"] = custom_start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_relative_offset(
            data: object,
        ) -> DashboardPreviousPeriodConfigRelativeOffsetType0Type0 | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                relative_offset_type_0_type_0 = DashboardPreviousPeriodConfigRelativeOffsetType0Type0(data)

                return relative_offset_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardPreviousPeriodConfigRelativeOffsetType0Type0 | int | None | Unset, data)

        relative_offset = _parse_relative_offset(d.pop("relativeOffset", UNSET))

        def _parse_custom_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                custom_start_time_type_0 = datetime.datetime.fromisoformat(data)

                return custom_start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        custom_start_time = _parse_custom_start_time(d.pop("customStartTime", UNSET))

        dashboard_previous_period_config = cls(
            relative_offset=relative_offset,
            custom_start_time=custom_start_time,
        )

        return dashboard_previous_period_config
