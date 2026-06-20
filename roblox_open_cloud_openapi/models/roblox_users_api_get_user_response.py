from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiGetUserResponse")


@_attrs_define
class RobloxUsersApiGetUserResponse:
    """A response model representing user information.

    Attributes:
        description (str | Unset): The user description.
        created (datetime.datetime | Unset): When the user signed up.
        is_banned (bool | Unset): Whether the user is banned
        external_app_display_name (str | Unset): Unused, legacy attribute. For now always null to not disturb existing
            client code that might rely on its existence.
        has_verified_badge (bool | Unset): The user's verified badge status.
        id (int | Unset): The user Id.
        name (str | Unset): The user name.
        display_name (str | Unset): The user DisplayName.
    """

    description: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    is_banned: bool | Unset = UNSET
    external_app_display_name: str | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        is_banned = self.is_banned

        external_app_display_name = self.external_app_display_name

        has_verified_badge = self.has_verified_badge

        id = self.id

        name = self.name

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if created is not UNSET:
            field_dict["created"] = created
        if is_banned is not UNSET:
            field_dict["isBanned"] = is_banned
        if external_app_display_name is not UNSET:
            field_dict["externalAppDisplayName"] = external_app_display_name
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
        description = d.pop("description", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        is_banned = d.pop("isBanned", UNSET)

        external_app_display_name = d.pop("externalAppDisplayName", UNSET)

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_users_api_get_user_response = cls(
            description=description,
            created=created,
            is_banned=is_banned,
            external_app_display_name=external_app_display_name,
            has_verified_badge=has_verified_badge,
            id=id,
            name=name,
            display_name=display_name,
        )

        return roblox_users_api_get_user_response
