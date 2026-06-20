from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.luau_execution_session_task_log import LuauExecutionSessionTaskLog


T = TypeVar("T", bound="ListLuauExecutionSessionTaskLogsResponse")


@_attrs_define
class ListLuauExecutionSessionTaskLogsResponse:
    """A list of LuauExecutionSessionTaskLogs in the parent collection.

    Attributes:
        luau_execution_session_task_logs (list[LuauExecutionSessionTaskLog] | Unset): The LuauExecutionSessionTaskLogs
            from the specified
            LuauExecutionSessionTask.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    luau_execution_session_task_logs: list[LuauExecutionSessionTaskLog] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        luau_execution_session_task_logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.luau_execution_session_task_logs, Unset):
            luau_execution_session_task_logs = []
            for luau_execution_session_task_logs_item_data in self.luau_execution_session_task_logs:
                luau_execution_session_task_logs_item = luau_execution_session_task_logs_item_data.to_dict()
                luau_execution_session_task_logs.append(luau_execution_session_task_logs_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if luau_execution_session_task_logs is not UNSET:
            field_dict["luauExecutionSessionTaskLogs"] = luau_execution_session_task_logs
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.luau_execution_session_task_log import LuauExecutionSessionTaskLog

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _luau_execution_session_task_logs = d.pop("luauExecutionSessionTaskLogs", UNSET)
        luau_execution_session_task_logs: list[LuauExecutionSessionTaskLog] | Unset = UNSET
        if _luau_execution_session_task_logs is not UNSET:
            luau_execution_session_task_logs = []
            for luau_execution_session_task_logs_item_data in _luau_execution_session_task_logs:
                luau_execution_session_task_logs_item = LuauExecutionSessionTaskLog.from_dict(
                    luau_execution_session_task_logs_item_data
                )

                luau_execution_session_task_logs.append(luau_execution_session_task_logs_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_luau_execution_session_task_logs_response = cls(
            luau_execution_session_task_logs=luau_execution_session_task_logs,
            next_page_token=next_page_token,
        )

        list_luau_execution_session_task_logs_response.additional_properties = d
        return list_luau_execution_session_task_logs_response

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
