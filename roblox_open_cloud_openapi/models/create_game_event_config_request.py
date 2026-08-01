from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.event_notification_audience import EventNotificationAudience
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGameEventConfigRequest")


@_attrs_define
class CreateGameEventConfigRequest:
    """Optional event configuration block (recurrence + notification audience) on the v3 Create body.

    Attributes:
        recurrence (None | str | Unset): Cron expression for recurrence. Null = no recurrence. Validated server-side.
        recurrence_end_time (datetime.datetime | None | Unset):
        notification_audience (EventNotificationAudience | None | Unset):
    """

    recurrence: None | str | Unset = UNSET
    recurrence_end_time: datetime.datetime | None | Unset = UNSET
    notification_audience: EventNotificationAudience | None | Unset = UNSET

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

        notification_audience: None | str | Unset
        if isinstance(self.notification_audience, Unset):
            notification_audience = UNSET
        elif isinstance(self.notification_audience, EventNotificationAudience):
            notification_audience = self.notification_audience.value
        else:
            notification_audience = self.notification_audience

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

        def _parse_notification_audience(data: object) -> EventNotificationAudience | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                notification_audience_type_1 = EventNotificationAudience(data)

                return notification_audience_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventNotificationAudience | None | Unset, data)

        notification_audience = _parse_notification_audience(d.pop("notificationAudience", UNSET))

        create_game_event_config_request = cls(
            recurrence=recurrence,
            recurrence_end_time=recurrence_end_time,
            notification_audience=notification_audience,
        )

        return create_game_event_config_request
