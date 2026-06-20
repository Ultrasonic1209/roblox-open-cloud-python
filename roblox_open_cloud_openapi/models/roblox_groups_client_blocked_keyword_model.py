from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsClientBlockedKeywordModel")


@_attrs_define
class RobloxGroupsClientBlockedKeywordModel:
    """
    Attributes:
        id (str | Unset):
        keyword (str | Unset):
        created_by (int | Unset):
        is_private (bool | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    keyword: str | Unset = UNSET
    created_by: int | Unset = UNSET
    is_private: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        keyword = self.keyword

        created_by = self.created_by

        is_private = self.is_private

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        keyword = d.pop("keyword", UNSET)

        created_by = d.pop("createdBy", UNSET)

        is_private = d.pop("isPrivate", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        roblox_groups_client_blocked_keyword_model = cls(
            id=id,
            keyword=keyword,
            created_by=created_by,
            is_private=is_private,
            created_at=created_at,
            updated_at=updated_at,
        )

        return roblox_groups_client_blocked_keyword_model
