from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel
    from ..models.roblox_groups_api_shout_response import RobloxGroupsApiShoutResponse


T = TypeVar("T", bound="RobloxGroupsApiGroupDetailResponse")


@_attrs_define
class RobloxGroupsApiGroupDetailResponse:
    """A detailed group response model

    Attributes:
        id (int | Unset): The group id
        name (str | Unset): The group name
        description (str | Unset): The group description
        owner (RobloxGroupsApiModelsResponseUserModel | Unset): A model representing data about an
            Roblox.Platform.Membership.IUser
        shout (RobloxGroupsApiShoutResponse | Unset):
        member_count (int | Unset): The number of members in the group
        is_builders_club_only (bool | Unset): Whether the group is Builders Club only
        public_entry_allowed (bool | Unset): Whether the group is public (no approval required)
        is_locked (bool | Unset): Whether the group is locked
        has_verified_badge (bool | Unset): Whether the group has a verified badge.
        has_social_modules (bool | Unset): Whether the group has social modules enabled (e.g. Forums)
            (determines if "Followers" vs "Members" should be shown).
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    owner: RobloxGroupsApiModelsResponseUserModel | Unset = UNSET
    shout: RobloxGroupsApiShoutResponse | Unset = UNSET
    member_count: int | Unset = UNSET
    is_builders_club_only: bool | Unset = UNSET
    public_entry_allowed: bool | Unset = UNSET
    is_locked: bool | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET
    has_social_modules: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        shout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shout, Unset):
            shout = self.shout.to_dict()

        member_count = self.member_count

        is_builders_club_only = self.is_builders_club_only

        public_entry_allowed = self.public_entry_allowed

        is_locked = self.is_locked

        has_verified_badge = self.has_verified_badge

        has_social_modules = self.has_social_modules

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if owner is not UNSET:
            field_dict["owner"] = owner
        if shout is not UNSET:
            field_dict["shout"] = shout
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if is_builders_club_only is not UNSET:
            field_dict["isBuildersClubOnly"] = is_builders_club_only
        if public_entry_allowed is not UNSET:
            field_dict["publicEntryAllowed"] = public_entry_allowed
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge
        if has_social_modules is not UNSET:
            field_dict["hasSocialModules"] = has_social_modules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_api_models_response_user_model import RobloxGroupsApiModelsResponseUserModel
        from ..models.roblox_groups_api_shout_response import RobloxGroupsApiShoutResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: RobloxGroupsApiModelsResponseUserModel | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = RobloxGroupsApiModelsResponseUserModel.from_dict(_owner)

        _shout = d.pop("shout", UNSET)
        shout: RobloxGroupsApiShoutResponse | Unset
        if isinstance(_shout, Unset):
            shout = UNSET
        else:
            shout = RobloxGroupsApiShoutResponse.from_dict(_shout)

        member_count = d.pop("memberCount", UNSET)

        is_builders_club_only = d.pop("isBuildersClubOnly", UNSET)

        public_entry_allowed = d.pop("publicEntryAllowed", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        has_social_modules = d.pop("hasSocialModules", UNSET)

        roblox_groups_api_group_detail_response = cls(
            id=id,
            name=name,
            description=description,
            owner=owner,
            shout=shout,
            member_count=member_count,
            is_builders_club_only=is_builders_club_only,
            public_entry_allowed=public_entry_allowed,
            is_locked=is_locked,
            has_verified_badge=has_verified_badge,
            has_social_modules=has_social_modules,
        )

        return roblox_groups_api_group_detail_response
