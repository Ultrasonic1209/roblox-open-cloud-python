from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1Schedule")


@_attrs_define
class InternalPublicV1Schedule:
    """
    Attributes:
        duration_in_days (int | Unset): How long the campaign runs from startTime, in days. Must not exceed 3650 (about
            10 years).
        end_time (str | Unset): Not accepted in v1 and never returned; supplying it returns 400. Use
            durationInDays to set when the campaign ends. Reserved for a future objective.
        start_time (str | Unset): The time the campaign starts serving, as an RFC 3339 UTC timestamp. On a create
            request it must not be in the past.
    """

    duration_in_days: int | Unset = UNSET
    end_time: str | Unset = UNSET
    start_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_in_days = self.duration_in_days

        end_time = self.end_time

        start_time = self.start_time

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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        duration_in_days = d.pop("durationInDays", UNSET)

        end_time = d.pop("endTime", UNSET)

        start_time = d.pop("startTime", UNSET)

        internal_public_v1_schedule = cls(
            duration_in_days=duration_in_days,
            end_time=end_time,
            start_time=start_time,
        )

        internal_public_v1_schedule.additional_properties = d
        return internal_public_v1_schedule

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
