from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleExperimentRequest")


@_attrs_define
class ScheduleExperimentRequest:
    """Request body for
    `POST /v1/experimentation/universes/{universeId}/experiments/{experimentId}:schedule`.

        Attributes:
            scheduled_start_time (None | str | Unset): UTC time at which the experiment should be auto-started.
    """

    scheduled_start_time: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scheduled_start_time: None | str | Unset
        if isinstance(self.scheduled_start_time, Unset):
            scheduled_start_time = UNSET
        else:
            scheduled_start_time = self.scheduled_start_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scheduled_start_time is not UNSET:
            field_dict["scheduledStartTime"] = scheduled_start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_scheduled_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduled_start_time = _parse_scheduled_start_time(d.pop("scheduledStartTime", UNSET))

        schedule_experiment_request = cls(
            scheduled_start_time=scheduled_start_time,
        )

        return schedule_experiment_request
