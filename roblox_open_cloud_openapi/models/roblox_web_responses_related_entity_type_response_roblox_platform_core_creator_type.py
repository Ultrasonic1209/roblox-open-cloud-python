from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_web_responses_related_entity_type_response_roblox_platform_core_creator_type_type import (
    RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorTypeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorType")


@_attrs_define
class RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorType:
    """
    Attributes:
        id (int | Unset):
        type_ (RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorTypeType | Unset):  ['User' = 0,
            'Group' = 1]
        name (str | Unset):
    """

    id: int | Unset = UNSET
    type_: RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorTypeType | Unset = UNSET
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
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorTypeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxWebResponsesRelatedEntityTypeResponseRobloxPlatformCoreCreatorTypeType(_type_)

        name = d.pop("name", UNSET)

        roblox_web_responses_related_entity_type_response_roblox_platform_core_creator_type = cls(
            id=id,
            type_=type_,
            name=name,
        )

        return roblox_web_responses_related_entity_type_response_roblox_platform_core_creator_type
