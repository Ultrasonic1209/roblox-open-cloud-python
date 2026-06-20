from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.luau_execution_session_task_log_log_message_message_type import (
    LuauExecutionSessionTaskLogLogMessageMessageType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LuauExecutionSessionTaskLogLogMessage")


@_attrs_define
class LuauExecutionSessionTaskLogLogMessage:
    """A single log message along with its associated metadata

    Attributes:
        message (str | Unset): The log message
        create_time (datetime.datetime | Unset): The time at which the log message was produced Example:
            2023-07-05T12:34:56Z.
        message_type (LuauExecutionSessionTaskLogLogMessageMessageType | Unset): The `MessageType` of the log message.

            Possible values:

              | Value | Description |
              | --- | --- |
              | MESSAGE_TYPE_UNSPECIFIED | UNSPECIFIED |
              | OUTPUT | Corresponds to the `MessageOutput` enum value of the engine API. |
              | INFO | Corresponds to the `MessageInfo` enum value of the engine API. |
              | WARNING | Corresponds to the `MessageWarning` enum value of the engine API. |
              | ERROR | Corresponds to the `MessageError` enum value of the engine API. | Example: MESSAGE_TYPE_UNSPECIFIED.
    """

    message: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    message_type: LuauExecutionSessionTaskLogLogMessageMessageType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        message_type: str | Unset = UNSET
        if not isinstance(self.message_type, Unset):
            message_type = self.message_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if message_type is not UNSET:
            field_dict["messageType"] = message_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        message = d.pop("message", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _message_type = d.pop("messageType", UNSET)
        message_type: LuauExecutionSessionTaskLogLogMessageMessageType | Unset
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = LuauExecutionSessionTaskLogLogMessageMessageType(_message_type)

        luau_execution_session_task_log_log_message = cls(
            message=message,
            create_time=create_time,
            message_type=message_type,
        )

        luau_execution_session_task_log_log_message.additional_properties = d
        return luau_execution_session_task_log_log_message

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
