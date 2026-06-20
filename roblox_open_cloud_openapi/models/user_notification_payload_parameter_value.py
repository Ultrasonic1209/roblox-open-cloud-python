from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserNotificationPayloadParameterValue")


@_attrs_define
class UserNotificationPayloadParameterValue:
    """A parameter value that a template uses to render a notification message.

    Attributes:
        string_value (str | Unset): A string value. Example: bronze egg.
        int_64_value (int | Unset): An int64 value. Example: 10101010.
    """

    string_value: str | Unset = UNSET
    int_64_value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        string_value = self.string_value

        int_64_value = self.int_64_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value
        if int_64_value is not UNSET:
            field_dict["int64Value"] = int_64_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        string_value = d.pop("stringValue", UNSET)

        int_64_value = d.pop("int64Value", UNSET)

        user_notification_payload_parameter_value = cls(
            string_value=string_value,
            int_64_value=int_64_value,
        )

        user_notification_payload_parameter_value.additional_properties = d
        return user_notification_payload_parameter_value

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
