from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_web_responses_related_entity_type_response_roblox_web_responses_groups_group_owner_type_type import (
    RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerTypeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerType")


@_attrs_define
class RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerType:
    """
    Attributes:
        id (int | Unset):
        type_ (RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerTypeType | Unset):  ['User'
            = 0]
        name (str | Unset):
    """

    id: int | Unset = UNSET
    type_: RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerTypeType | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: int | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerTypeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxWebResponsesRelatedEntityTypeResponseRobloxWebResponsesGroupsGroupOwnerTypeType(_type_)

        name = d.pop("name", UNSET)

        roblox_web_responses_related_entity_type_response_roblox_web_responses_groups_group_owner_type = cls(
            id=id,
            type_=type_,
            name=name,
        )

        return roblox_web_responses_related_entity_type_response_roblox_web_responses_groups_group_owner_type
