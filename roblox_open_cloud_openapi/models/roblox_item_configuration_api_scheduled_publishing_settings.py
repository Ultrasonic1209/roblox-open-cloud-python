from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiScheduledPublishingSettings")


@_attrs_define
class RobloxItemConfigurationApiScheduledPublishingSettings:
    """
    Attributes:
        scheduled_publish_max_time_in_advance_time_span (str | Unset): The maximum time in the future that a scheduled
            publish can be set.
        scheduled_publish_min_duration_time_span (str | Unset): The minimum time in between scheduled publishes.
    """

    scheduled_publish_max_time_in_advance_time_span: str | Unset = UNSET
    scheduled_publish_min_duration_time_span: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scheduled_publish_max_time_in_advance_time_span = self.scheduled_publish_max_time_in_advance_time_span

        scheduled_publish_min_duration_time_span = self.scheduled_publish_min_duration_time_span

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scheduled_publish_max_time_in_advance_time_span is not UNSET:
            field_dict["scheduledPublishMaxTimeInAdvanceTimeSpan"] = scheduled_publish_max_time_in_advance_time_span
        if scheduled_publish_min_duration_time_span is not UNSET:
            field_dict["scheduledPublishMinDurationTimeSpan"] = scheduled_publish_min_duration_time_span

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheduled_publish_max_time_in_advance_time_span = d.pop("scheduledPublishMaxTimeInAdvanceTimeSpan", UNSET)

        scheduled_publish_min_duration_time_span = d.pop("scheduledPublishMinDurationTimeSpan", UNSET)

        roblox_item_configuration_api_scheduled_publishing_settings = cls(
            scheduled_publish_max_time_in_advance_time_span=scheduled_publish_max_time_in_advance_time_span,
            scheduled_publish_min_duration_time_span=scheduled_publish_min_duration_time_span,
        )

        return roblox_item_configuration_api_scheduled_publishing_settings
