from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemBadgeDetails")


@_attrs_define
class InventoryItemBadgeDetails:
    """Specific fields that are applicable to a badge.

    Attributes:
        badge_id (str | Unset): A unique ID that identifies a badge.
    """

    badge_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        badge_id = self.badge_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if badge_id is not UNSET:
            field_dict["badgeId"] = badge_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        badge_id = d.pop("badgeId", UNSET)

        inventory_item_badge_details = cls(
            badge_id=badge_id,
        )

        return inventory_item_badge_details
