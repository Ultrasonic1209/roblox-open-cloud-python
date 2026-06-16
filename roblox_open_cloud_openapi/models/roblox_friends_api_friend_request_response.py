from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_friends_api_friend_request import RobloxFriendsApiFriendRequest


T = TypeVar("T", bound="RobloxFriendsApiFriendRequestResponse")


@_attrs_define
class RobloxFriendsApiFriendRequestResponse:
    """A response model representing a friend request.

    Attributes:
        friend_request (RobloxFriendsApiFriendRequest | Unset): A response model representing a friend request.
        mutual_friends_list (list[str] | Unset): mutualFriendsList
        has_verified_badge (bool | Unset): The user's verified badge status.
        description (str | Unset): The user description.
        created (datetime.datetime | Unset): When the user signed up.
        is_banned (bool | Unset): Whether or not the user is banned
        external_app_display_name (str | Unset): Used when user is logged in from third party app (e.g. QQ)
            ExternalAppDisplayName is the name used in that app (e.g. QQ nickname)
        id (int | Unset): The user Id.
        name (str | Unset): The user name.
        display_name (str | Unset): The user DisplayName.
    """

    friend_request: RobloxFriendsApiFriendRequest | Unset = UNSET
    mutual_friends_list: list[str] | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET
    description: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    is_banned: bool | Unset = UNSET
    external_app_display_name: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        friend_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.friend_request, Unset):
            friend_request = self.friend_request.to_dict()

        mutual_friends_list: list[str] | Unset = UNSET
        if not isinstance(self.mutual_friends_list, Unset):
            mutual_friends_list = self.mutual_friends_list

        has_verified_badge = self.has_verified_badge

        description = self.description

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        is_banned = self.is_banned

        external_app_display_name = self.external_app_display_name

        id = self.id

        name = self.name

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if friend_request is not UNSET:
            field_dict["friendRequest"] = friend_request
        if mutual_friends_list is not UNSET:
            field_dict["mutualFriendsList"] = mutual_friends_list
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge
        if description is not UNSET:
            field_dict["description"] = description
        if created is not UNSET:
            field_dict["created"] = created
        if is_banned is not UNSET:
            field_dict["isBanned"] = is_banned
        if external_app_display_name is not UNSET:
            field_dict["externalAppDisplayName"] = external_app_display_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_friends_api_friend_request import RobloxFriendsApiFriendRequest

        d = dict(src_dict)
        _friend_request = d.pop("friendRequest", UNSET)
        friend_request: RobloxFriendsApiFriendRequest | Unset
        if isinstance(_friend_request, Unset):
            friend_request = UNSET
        else:
            friend_request = RobloxFriendsApiFriendRequest.from_dict(_friend_request)

        mutual_friends_list = cast(list[str], d.pop("mutualFriendsList", UNSET))

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        description = d.pop("description", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        is_banned = d.pop("isBanned", UNSET)

        external_app_display_name = d.pop("externalAppDisplayName", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_friends_api_friend_request_response = cls(
            friend_request=friend_request,
            mutual_friends_list=mutual_friends_list,
            has_verified_badge=has_verified_badge,
            description=description,
            created=created,
            is_banned=is_banned,
            external_app_display_name=external_app_display_name,
            id=id,
            name=name,
            display_name=display_name,
        )

        return roblox_friends_api_friend_request_response
