from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_friends_api_models_response_user_response_presence_type import (
    RobloxFriendsApiModelsResponseUserResponsePresenceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiModelsResponseUserResponse")


@_attrs_define
class RobloxFriendsApiModelsResponseUserResponse:
    """A response model representing user information that also contains select presence information

    Attributes:
        is_online (bool | Unset): Whether the user is online.
        presence_type (RobloxFriendsApiModelsResponseUserResponsePresenceType | Unset): Where the user is online.
        is_deleted (bool | Unset): Whether the user is deleted.
        friend_frequent_score (int | Unset): Frequents value for the user.
        friend_frequent_rank (int | Unset): Frequents rank for the user.
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

    is_online: bool | Unset = UNSET
    presence_type: RobloxFriendsApiModelsResponseUserResponsePresenceType | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    friend_frequent_score: int | Unset = UNSET
    friend_frequent_rank: int | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET
    description: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    is_banned: bool | Unset = UNSET
    external_app_display_name: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_online = self.is_online

        presence_type: int | Unset = UNSET
        if not isinstance(self.presence_type, Unset):
            presence_type = self.presence_type.value

        is_deleted = self.is_deleted

        friend_frequent_score = self.friend_frequent_score

        friend_frequent_rank = self.friend_frequent_rank

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
        if is_online is not UNSET:
            field_dict["isOnline"] = is_online
        if presence_type is not UNSET:
            field_dict["presenceType"] = presence_type
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if friend_frequent_score is not UNSET:
            field_dict["friendFrequentScore"] = friend_frequent_score
        if friend_frequent_rank is not UNSET:
            field_dict["friendFrequentRank"] = friend_frequent_rank
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
        d = dict(src_dict)
        is_online = d.pop("isOnline", UNSET)

        _presence_type = d.pop("presenceType", UNSET)
        presence_type: RobloxFriendsApiModelsResponseUserResponsePresenceType | Unset
        if isinstance(_presence_type, Unset):
            presence_type = UNSET
        else:
            presence_type = RobloxFriendsApiModelsResponseUserResponsePresenceType(_presence_type)

        is_deleted = d.pop("isDeleted", UNSET)

        friend_frequent_score = d.pop("friendFrequentScore", UNSET)

        friend_frequent_rank = d.pop("friendFrequentRank", UNSET)

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

        roblox_friends_api_models_response_user_response = cls(
            is_online=is_online,
            presence_type=presence_type,
            is_deleted=is_deleted,
            friend_frequent_score=friend_frequent_score,
            friend_frequent_rank=friend_frequent_rank,
            has_verified_badge=has_verified_badge,
            description=description,
            created=created,
            is_banned=is_banned,
            external_app_display_name=external_app_display_name,
            id=id,
            name=name,
            display_name=display_name,
        )

        return roblox_friends_api_models_response_user_response
