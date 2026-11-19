from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DashboardNoTimeRangeOptions")


@_attrs_define
class DashboardNoTimeRangeOptions:
    """DashboardNoTimeRangeOptions disables time range controls for a surface."""

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        dashboard_no_time_range_options = cls()

        return dashboard_no_time_range_options
