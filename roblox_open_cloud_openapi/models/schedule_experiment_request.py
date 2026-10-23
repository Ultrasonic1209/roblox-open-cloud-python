from __future__ import annotations

import datetime
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
            scheduled_start_time (datetime.datetime | None | Unset): UTC time at which the experiment should be auto-
                started.
    """

    scheduled_start_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scheduled_start_time: None | str | Unset
        if isinstance(self.scheduled_start_time, Unset):
            scheduled_start_time = UNSET
        elif isinstance(self.scheduled_start_time, datetime.datetime):
            scheduled_start_time = self.scheduled_start_time.isoformat()
        else:
            scheduled_start_time = self.scheduled_start_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scheduled_start_time is not UNSET:
            field_dict["scheduledStartTime"] = scheduled_start_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_scheduled_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_start_time_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_start_time = _parse_scheduled_start_time(d.pop("scheduledStartTime", UNSET))

        schedule_experiment_request = cls(
            scheduled_start_time=scheduled_start_time,
        )

        return schedule_experiment_request
