from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxEconomyApiChartDataPointResponse")


@_attrs_define
class RobloxEconomyApiChartDataPointResponse:
    """Chart data point.

    Attributes:
        value (int | Unset): The value of the data point.
        date (datetime.datetime | Unset): The date associated with the data point.
    """

    value: int | Unset = UNSET
    date: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.datetime.fromisoformat(_date)

        roblox_economy_api_chart_data_point_response = cls(
            value=value,
            date=date,
        )

        return roblox_economy_api_chart_data_point_response
