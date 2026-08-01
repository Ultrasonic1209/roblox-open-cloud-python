from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.event_notification_audience import EventNotificationAudience
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigResponse")


@_attrs_define
class ConfigResponse:
    """
    Attributes:
        recurrence (None | str | Unset): Cron expression defining the event's recurrence schedule, if any.
        recurrence_end_time (datetime.datetime | None | Unset): The latest UTC timestamp at which automatic recurrence
            scheduling can occur.
        notification_audience (EventNotificationAudience | Unset): The notification audience for an experience event
    """

    recurrence: None | str | Unset = UNSET
    recurrence_end_time: datetime.datetime | None | Unset = UNSET
    notification_audience: EventNotificationAudience | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recurrence: None | str | Unset
        if isinstance(self.recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = self.recurrence

        recurrence_end_time: None | str | Unset
        if isinstance(self.recurrence_end_time, Unset):
            recurrence_end_time = UNSET
        elif isinstance(self.recurrence_end_time, datetime.datetime):
            recurrence_end_time = self.recurrence_end_time.isoformat()
        else:
            recurrence_end_time = self.recurrence_end_time

        notification_audience: str | Unset = UNSET
        if not isinstance(self.notification_audience, Unset):
            notification_audience = self.notification_audience.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if recurrence_end_time is not UNSET:
            field_dict["recurrenceEndTime"] = recurrence_end_time
        if notification_audience is not UNSET:
            field_dict["notificationAudience"] = notification_audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_recurrence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recurrence = _parse_recurrence(d.pop("recurrence", UNSET))

        def _parse_recurrence_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recurrence_end_time_type_0 = datetime.datetime.fromisoformat(data)

                return recurrence_end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        recurrence_end_time = _parse_recurrence_end_time(d.pop("recurrenceEndTime", UNSET))

        _notification_audience = d.pop("notificationAudience", UNSET)
        notification_audience: EventNotificationAudience | Unset
        if isinstance(_notification_audience, Unset):
            notification_audience = UNSET
        else:
            notification_audience = EventNotificationAudience(_notification_audience)

        config_response = cls(
            recurrence=recurrence,
            recurrence_end_time=recurrence_end_time,
            notification_audience=notification_audience,
        )

        return config_response
