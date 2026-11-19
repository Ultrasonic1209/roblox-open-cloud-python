from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Schedule")


@_attrs_define
class Schedule:
    """
    Attributes:
        duration_in_days (int): How long the campaign runs from startTime, in days. Must not exceed 3650 (about
            10 years). Zero means the campaign has no end date and runs until you pause or
            cancel it; endTime is then omitted. A LIFETIME budget needs an end date, so it
            needs a positive value.
        start_time (datetime.datetime): The time the campaign starts serving, as an RFC 3339 timestamp. UTC (`Z`) is
            recommended. On a create request it must not be in the past.
        end_time (datetime.datetime | Unset): The instant the campaign stops, as an RFC 3339 UTC timestamp (read-only):
            one
            second before local midnight at the end of day durationInDays in the account's
            time zone. Not accepted on requests; supplying it returns 400. Use durationInDays
            to set when the campaign ends.
    """

    duration_in_days: int
    start_time: datetime.datetime
    end_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_in_days = self.duration_in_days

        start_time = self.start_time.isoformat()

        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "durationInDays": duration_in_days,
                "startTime": start_time,
            }
        )
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_in_days = d.pop("durationInDays")

        start_time = datetime.datetime.fromisoformat(d.pop("startTime"))

        _end_time = d.pop("endTime", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = datetime.datetime.fromisoformat(_end_time)

        schedule = cls(
            duration_in_days=duration_in_days,
            start_time=start_time,
            end_time=end_time,
        )

        schedule.additional_properties = d
        return schedule

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
