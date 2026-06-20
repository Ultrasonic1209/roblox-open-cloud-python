from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiMultiGetUserResponse")


@_attrs_define
class RobloxUsersApiMultiGetUserResponse:
    """<p>A response model specific to multi-get user.</p>
    <p>
                Note: Currently the MultiGet responses don't have all the data that the single gets have, to reduce
    payload size!
                We might want to revisit this decision in the future.
                </p>

        Attributes:
            has_verified_badge (bool | Unset): The user's verified badge status.
            id (int | Unset): The user Id.
            name (str | Unset): The user name.
            display_name (str | Unset): The user DisplayName.
    """

    has_verified_badge: bool | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        has_verified_badge = self.has_verified_badge

        id = self.id

        name = self.name

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_users_api_multi_get_user_response = cls(
            has_verified_badge=has_verified_badge,
            id=id,
            name=name,
            display_name=display_name,
        )

        return roblox_users_api_multi_get_user_response
