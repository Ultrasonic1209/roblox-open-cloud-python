from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiModelsResponseGroupNameHistoryResponseItem")


@_attrs_define
class RobloxGroupsApiModelsResponseGroupNameHistoryResponseItem:
    """A group name history response model

    Attributes:
        name (str | Unset): The group name before the change
        created (datetime.datetime | Unset): Date the name change was applied
    """

    name: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        roblox_groups_api_models_response_group_name_history_response_item = cls(
            name=name,
            created=created,
        )

        return roblox_groups_api_models_response_group_name_history_response_item
