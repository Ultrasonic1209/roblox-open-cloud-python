from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_translation_roles_api_assignee_type import RobloxTranslationRolesApiAssigneeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTranslationRolesApiAssignee")


@_attrs_define
class RobloxTranslationRolesApiAssignee:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        type_ (RobloxTranslationRolesApiAssigneeType | Unset):  ['User' = 0, 'Group' = 1, 'GroupRole' = 2]
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: RobloxTranslationRolesApiAssigneeType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RobloxTranslationRolesApiAssigneeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RobloxTranslationRolesApiAssigneeType(_type_)

        roblox_translation_roles_api_assignee = cls(
            id=id,
            name=name,
            type_=type_,
        )

        return roblox_translation_roles_api_assignee
