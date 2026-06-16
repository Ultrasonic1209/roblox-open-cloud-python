from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_restriction_log import UserRestrictionLog


T = TypeVar("T", bound="ListUserRestrictionLogsResponse")


@_attrs_define
class ListUserRestrictionLogsResponse:
    """Returns a list of change logs applied to UserRestriction resources.

    Attributes:
        logs (list[UserRestrictionLog] | Unset): The UserRestrictionLogs from the specified Universe.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    logs: list[UserRestrictionLog] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logs is not UNSET:
            field_dict["logs"] = logs
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_restriction_log import UserRestrictionLog

        d = dict(src_dict)
        _logs = d.pop("logs", UNSET)
        logs: list[UserRestrictionLog] | Unset = UNSET
        if _logs is not UNSET:
            logs = []
            for logs_item_data in _logs:
                logs_item = UserRestrictionLog.from_dict(logs_item_data)

                logs.append(logs_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_user_restriction_logs_response = cls(
            logs=logs,
            next_page_token=next_page_token,
        )

        list_user_restriction_logs_response.additional_properties = d
        return list_user_restriction_logs_response

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
