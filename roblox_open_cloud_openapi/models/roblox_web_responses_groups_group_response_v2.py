from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_web_responses_related_entity_type_response_roblox_web_responses_groups_group_owner_type import (
        RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerType,
    )


T = TypeVar("T", bound="RobloxWebResponsesGroupsGroupResponseV2")


@_attrs_define
class RobloxWebResponsesGroupsGroupResponseV2:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        description (str | Unset):
        owner (RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerType | Unset):
        member_count (int | Unset):
        created (datetime.datetime | Unset):
        has_verified_badge (bool | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    owner: RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerType | Unset = UNSET
    member_count: int | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        member_count = self.member_count

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        has_verified_badge = self.has_verified_badge

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
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if created is not UNSET:
            field_dict["created"] = created
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_web_responses_related_entity_type_response_roblox_web_responses_groups_group_owner_type import (
            RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerType,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerType | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerType.from_dict(_owner)

        member_count = d.pop("memberCount", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        roblox_web_responses_groups_group_response_v2 = cls(
            id=id,
            name=name,
            description=description,
            owner=owner,
            member_count=member_count,
            created=created,
            has_verified_badge=has_verified_badge,
        )

        return roblox_web_responses_groups_group_response_v2
