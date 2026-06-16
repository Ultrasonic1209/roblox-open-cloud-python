from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryItemBadgeDetails")


@_attrs_define
class InventoryItemBadgeDetails:
    """Specific fields that are applicable to a badge.

    Attributes:
        badge_id (str | Unset): A unique ID that identifies a badge. Example: 119925991.
    """

    badge_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        badge_id = self.badge_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if badge_id is not UNSET:
            field_dict["badgeId"] = badge_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        badge_id = d.pop("badgeId", UNSET)

        inventory_item_badge_details = cls(
            badge_id=badge_id,
        )

        inventory_item_badge_details.additional_properties = d
        return inventory_item_badge_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
