from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiAuthenticatedGetUserResponse")


@_attrs_define
class RobloxUsersApiAuthenticatedGetUserResponse:
    """A response model representing absolute minimal authenticating user information.
    No new attributes should be added to this response since it is in the critical path of app launch and we want to
    minimize dependencies.

        Attributes:
            id (int | Unset): The user Id.
            name (str | Unset): The user name.
            display_name (str | Unset): The user DisplayName.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_users_api_authenticated_get_user_response = cls(
            id=id,
            name=name,
            display_name=display_name,
        )

        return roblox_users_api_authenticated_get_user_response
