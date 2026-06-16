from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_role import GroupRole


T = TypeVar("T", bound="ListGroupRolesResponse")


@_attrs_define
class ListGroupRolesResponse:
    """A list of GroupRoles in the parent collection.

    Attributes:
        group_roles (list[GroupRole] | Unset): The GroupRoles from the specified Group.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    group_roles: list[GroupRole] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_roles, Unset):
            group_roles = []
            for group_roles_item_data in self.group_roles:
                group_roles_item = group_roles_item_data.to_dict()
                group_roles.append(group_roles_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_roles is not UNSET:
            field_dict["groupRoles"] = group_roles
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_role import GroupRole

        d = dict(src_dict)
        _group_roles = d.pop("groupRoles", UNSET)
        group_roles: list[GroupRole] | Unset = UNSET
        if _group_roles is not UNSET:
            group_roles = []
            for group_roles_item_data in _group_roles:
                group_roles_item = GroupRole.from_dict(group_roles_item_data)

                group_roles.append(group_roles_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_group_roles_response = cls(
            group_roles=group_roles,
            next_page_token=next_page_token,
        )

        list_group_roles_response.additional_properties = d
        return list_group_roles_response

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
