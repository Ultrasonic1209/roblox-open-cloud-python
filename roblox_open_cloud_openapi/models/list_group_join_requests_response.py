from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_join_request import GroupJoinRequest


T = TypeVar("T", bound="ListGroupJoinRequestsResponse")


@_attrs_define
class ListGroupJoinRequestsResponse:
    """A list of GroupJoinRequests in the parent collection.

    Attributes:
        group_join_requests (list[GroupJoinRequest] | Unset): The GroupJoinRequests from the specified Group.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    group_join_requests: list[GroupJoinRequest] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_join_requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_join_requests, Unset):
            group_join_requests = []
            for group_join_requests_item_data in self.group_join_requests:
                group_join_requests_item = group_join_requests_item_data.to_dict()
                group_join_requests.append(group_join_requests_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_join_requests is not UNSET:
            field_dict["groupJoinRequests"] = group_join_requests
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_join_request import GroupJoinRequest

        d = dict(src_dict)
        _group_join_requests = d.pop("groupJoinRequests", UNSET)
        group_join_requests: list[GroupJoinRequest] | Unset = UNSET
        if _group_join_requests is not UNSET:
            group_join_requests = []
            for group_join_requests_item_data in _group_join_requests:
                group_join_requests_item = GroupJoinRequest.from_dict(group_join_requests_item_data)

                group_join_requests.append(group_join_requests_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_group_join_requests_response = cls(
            group_join_requests=group_join_requests,
            next_page_token=next_page_token,
        )

        list_group_join_requests_response.additional_properties = d
        return list_group_join_requests_response

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
