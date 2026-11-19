from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportNotificationRequest")


@_attrs_define
class ReportNotificationRequest:
    """
    Attributes:
        notification_id (None | str | Unset):
    """

    notification_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        notification_id: None | str | Unset
        if isinstance(self.notification_id, Unset):
            notification_id = UNSET
        else:
            notification_id = self.notification_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if notification_id is not UNSET:
            field_dict["notificationId"] = notification_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_notification_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_id = _parse_notification_id(d.pop("notificationId", UNSET))

        report_notification_request = cls(
            notification_id=notification_id,
        )

        return report_notification_request
