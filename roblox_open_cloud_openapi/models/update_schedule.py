from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSchedule")


@_attrs_define
class UpdateSchedule:
    """
    Attributes:
        duration_in_days (int | Unset): The new duration from startTime, in days. Zero means the campaign has no end
            date.
        end_time (datetime.datetime | Unset): End time is read-only and is rejected when supplied in a request.
        start_time (datetime.datetime | Unset): The new campaign start time, as an RFC 3339 timestamp. UTC (`Z`) is
            recommended.
    """

    duration_in_days: int | Unset = UNSET
    end_time: datetime.datetime | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_in_days = self.duration_in_days

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration_in_days is not UNSET:
            field_dict["durationInDays"] = duration_in_days
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_in_days = d.pop("durationInDays", UNSET)

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = datetime.datetime.fromisoformat(_end_time)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = datetime.datetime.fromisoformat(_start_time)

        update_schedule = cls(
            duration_in_days=duration_in_days,
            end_time=end_time,
            start_time=start_time,
        )

        update_schedule.additional_properties = d
        return update_schedule

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
