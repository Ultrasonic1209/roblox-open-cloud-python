from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiRobloxBadgeResponse")


@_attrs_define
class RobloxAccountInformationApiRobloxBadgeResponse:
    """
    Attributes:
        id (int | Unset): The ID belonging to this Roblox badge.
        name (str | Unset): The name of this Roblox badge.
        description (str | Unset): The description belonging to this Roblox badge.
        image_url (str | Unset): The URL corresponding to the image which represents this Roblox badge.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    image_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        image_url = self.image_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        roblox_account_information_api_roblox_badge_response = cls(
            id=id,
            name=name,
            description=description,
            image_url=image_url,
        )

        return roblox_account_information_api_roblox_badge_response
