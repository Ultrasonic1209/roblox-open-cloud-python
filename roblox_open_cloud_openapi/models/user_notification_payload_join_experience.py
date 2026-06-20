from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserNotificationPayloadJoinExperience")


@_attrs_define
class UserNotificationPayloadJoinExperience:
    """A call-to-action that represents joining an experience.

    Attributes:
        launch_data (str | Unset): Arbitrary data that is available to an experience
            when a user joins the experience with the notification.

            This value is limited to a maximum of 200 bytes. Example: Launch Data.
    """

    launch_data: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        launch_data = self.launch_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if launch_data is not UNSET:
            field_dict["launchData"] = launch_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        launch_data = d.pop("launchData", UNSET)

        user_notification_payload_join_experience = cls(
            launch_data=launch_data,
        )

        user_notification_payload_join_experience.additional_properties = d
        return user_notification_payload_join_experience

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
