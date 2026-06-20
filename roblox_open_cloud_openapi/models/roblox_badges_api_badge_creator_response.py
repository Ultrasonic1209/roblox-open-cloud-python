from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxBadgesApiBadgeCreatorResponse")


@_attrs_define
class RobloxBadgesApiBadgeCreatorResponse:
    """Represents information about the badge creator. (Creator of the place that awarded the badge)

    Attributes:
        id (int | Unset): The creator ID
        name (str | Unset): The name of the creator
        type_ (str | Unset): The type of the creator
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

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
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        roblox_badges_api_badge_creator_response = cls(
            id=id,
            name=name,
            type_=type_,
        )

        return roblox_badges_api_badge_creator_response
