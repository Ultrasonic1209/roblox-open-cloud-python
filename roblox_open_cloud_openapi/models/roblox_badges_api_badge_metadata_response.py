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
        default_badge_icon_image_id (int | Unset): The asset ID of the curated default badge icon used when a badge is
            created without an
            uploaded icon file, or `0` when the default badge icon feature is disabled.
    """

    badge_creation_price: int | Unset = UNSET
    max_badge_name_length: int | Unset = UNSET
    max_badge_description_length: int | Unset = UNSET
    default_badge_icon_image_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        badge_creation_price = self.badge_creation_price

        max_badge_name_length = self.max_badge_name_length

        max_badge_description_length = self.max_badge_description_length

        default_badge_icon_image_id = self.default_badge_icon_image_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if badge_creation_price is not UNSET:
            field_dict["badgeCreationPrice"] = badge_creation_price
        if max_badge_name_length is not UNSET:
            field_dict["maxBadgeNameLength"] = max_badge_name_length
        if max_badge_description_length is not UNSET:
            field_dict["maxBadgeDescriptionLength"] = max_badge_description_length
        if default_badge_icon_image_id is not UNSET:
            field_dict["defaultBadgeIconImageId"] = default_badge_icon_image_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        badge_creation_price = d.pop("badgeCreationPrice", UNSET)

        max_badge_name_length = d.pop("maxBadgeNameLength", UNSET)

        max_badge_description_length = d.pop("maxBadgeDescriptionLength", UNSET)

        default_badge_icon_image_id = d.pop("defaultBadgeIconImageId", UNSET)

        roblox_badges_api_badge_metadata_response = cls(
            badge_creation_price=badge_creation_price,
            max_badge_name_length=max_badge_name_length,
            max_badge_description_length=max_badge_description_length,
            default_badge_icon_image_id=default_badge_icon_image_id,
        )

        return roblox_badges_api_badge_metadata_response
