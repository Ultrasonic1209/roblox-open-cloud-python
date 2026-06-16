from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxBadgesApiBadgeMetadataResponse")


@_attrs_define
class RobloxBadgesApiBadgeMetadataResponse:
    """Metadata about badges.

    Attributes:
        badge_creation_price (int | Unset): The cost in Robux for creating a new badge.
        max_badge_name_length (int | Unset): The max length for a badge name.
        max_badge_description_length (int | Unset): The max length for a badge description.
    """

    badge_creation_price: int | Unset = UNSET
    max_badge_name_length: int | Unset = UNSET
    max_badge_description_length: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        badge_creation_price = self.badge_creation_price

        max_badge_name_length = self.max_badge_name_length

        max_badge_description_length = self.max_badge_description_length

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if badge_creation_price is not UNSET:
            field_dict["badgeCreationPrice"] = badge_creation_price
        if max_badge_name_length is not UNSET:
            field_dict["maxBadgeNameLength"] = max_badge_name_length
        if max_badge_description_length is not UNSET:
            field_dict["maxBadgeDescriptionLength"] = max_badge_description_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        badge_creation_price = d.pop("badgeCreationPrice", UNSET)

        max_badge_name_length = d.pop("maxBadgeNameLength", UNSET)

        max_badge_description_length = d.pop("maxBadgeDescriptionLength", UNSET)

        roblox_badges_api_badge_metadata_response = cls(
            badge_creation_price=badge_creation_price,
            max_badge_name_length=max_badge_name_length,
            max_badge_description_length=max_badge_description_length,
        )

        return roblox_badges_api_badge_metadata_response
