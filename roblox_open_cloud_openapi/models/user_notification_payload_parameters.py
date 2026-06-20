from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_notification_payload_parameter_value import UserNotificationPayloadParameterValue


T = TypeVar("T", bound="UserNotificationPayloadParameters")


@_attrs_define
class UserNotificationPayloadParameters:
    """A map of parameters used to render a notification message template.

    For example, given a template of `Your {egg_name} just hatched.` with
    parameters of `[{"egg_name": {"string_value": "royal egg"}}]`, the
    rendered notification message is: `Your royal egg just hatched.`

    """

    additional_properties: dict[str, UserNotificationPayloadParameterValue] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_notification_payload_parameter_value import UserNotificationPayloadParameterValue

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_notification_payload_parameters = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = UserNotificationPayloadParameterValue.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        user_notification_payload_parameters.additional_properties = additional_properties
        return user_notification_payload_parameters

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> UserNotificationPayloadParameterValue:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: UserNotificationPayloadParameterValue) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
