from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiGroupSearchResponseItem")


@_attrs_define
class RobloxGroupsApiGroupSearchResponseItem:
    """A group search response

    Attributes:
        id (int | Unset): The group id
        name (str | Unset): The group name
        description (str | Unset): The group description
        member_count (int | Unset): The number of members in the group
        previous_name (str | Unset): The previous name of the group
        public_entry_allowed (bool | Unset): When true anyone can join the group. When false manual approval
            is required to join the group
        created (datetime.datetime | Unset): When the group was created
        updated (datetime.datetime | Unset): When the group was last updated
        has_verified_badge (bool | Unset): The group's verified badge status
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    member_count: int | Unset = UNSET
    previous_name: str | Unset = UNSET
    public_entry_allowed: bool | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        member_count = self.member_count

        previous_name = self.previous_name

        public_entry_allowed = self.public_entry_allowed

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        has_verified_badge = self.has_verified_badge

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if previous_name is not UNSET:
            field_dict["previousName"] = previous_name
        if public_entry_allowed is not UNSET:
            field_dict["publicEntryAllowed"] = public_entry_allowed
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        member_count = d.pop("memberCount", UNSET)

        previous_name = d.pop("previousName", UNSET)

        public_entry_allowed = d.pop("publicEntryAllowed", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        roblox_groups_api_group_search_response_item = cls(
            id=id,
            name=name,
            description=description,
            member_count=member_count,
            previous_name=previous_name,
            public_entry_allowed=public_entry_allowed,
            created=created,
            updated=updated,
            has_verified_badge=has_verified_badge,
        )

        return roblox_groups_api_group_search_response_item
