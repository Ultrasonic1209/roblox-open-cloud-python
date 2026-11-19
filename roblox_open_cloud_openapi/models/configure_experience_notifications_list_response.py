from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configure_experience_notification_response import ConfigureExperienceNotificationResponse


T = TypeVar("T", bound="ConfigureExperienceNotificationsListResponse")


@_attrs_define
class ConfigureExperienceNotificationsListResponse:
    """
    Attributes:
        notification_string_configs (list[ConfigureExperienceNotificationResponse] | None | Unset):
        previous_page_cursor (None | str | Unset):
        next_page_cursor (None | str | Unset):
    """

    notification_string_configs: list[ConfigureExperienceNotificationResponse] | None | Unset = UNSET
    previous_page_cursor: None | str | Unset = UNSET
    next_page_cursor: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        notification_string_configs: list[dict[str, Any]] | None | Unset
        if isinstance(self.notification_string_configs, Unset):
            notification_string_configs = UNSET
        elif isinstance(self.notification_string_configs, list):
            notification_string_configs = []
            for notification_string_configs_type_0_item_data in self.notification_string_configs:
                notification_string_configs_type_0_item = notification_string_configs_type_0_item_data.to_dict()
                notification_string_configs.append(notification_string_configs_type_0_item)

        else:
            notification_string_configs = self.notification_string_configs

        previous_page_cursor: None | str | Unset
        if isinstance(self.previous_page_cursor, Unset):
            previous_page_cursor = UNSET
        else:
            previous_page_cursor = self.previous_page_cursor

        next_page_cursor: None | str | Unset
        if isinstance(self.next_page_cursor, Unset):
            next_page_cursor = UNSET
        else:
            next_page_cursor = self.next_page_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if notification_string_configs is not UNSET:
            field_dict["notificationStringConfigs"] = notification_string_configs
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configure_experience_notification_response import ConfigureExperienceNotificationResponse  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_notification_string_configs(
            data: object,
        ) -> list[ConfigureExperienceNotificationResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_string_configs_type_0 = []
                _notification_string_configs_type_0 = data
                for notification_string_configs_type_0_item_data in _notification_string_configs_type_0:
                    notification_string_configs_type_0_item = ConfigureExperienceNotificationResponse.from_dict(
                        notification_string_configs_type_0_item_data
                    )

                    notification_string_configs_type_0.append(notification_string_configs_type_0_item)

                return notification_string_configs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConfigureExperienceNotificationResponse] | None | Unset, data)

        notification_string_configs = _parse_notification_string_configs(d.pop("notificationStringConfigs", UNSET))

        def _parse_previous_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_page_cursor = _parse_previous_page_cursor(d.pop("previousPageCursor", UNSET))

        def _parse_next_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_cursor = _parse_next_page_cursor(d.pop("nextPageCursor", UNSET))

        configure_experience_notifications_list_response = cls(
            notification_string_configs=notification_string_configs,
            previous_page_cursor=previous_page_cursor,
            next_page_cursor=next_page_cursor,
        )

        return configure_experience_notifications_list_response
