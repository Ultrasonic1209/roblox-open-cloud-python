from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_item import InventoryItem


T = TypeVar("T", bound="ListInventoryItemsResponse")


@_attrs_define
class ListInventoryItemsResponse:
    """A list of InventoryItems in the parent collection.

    Attributes:
        inventory_items (list[InventoryItem] | Unset): The InventoryItems from the specified User.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    inventory_items: list[InventoryItem] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inventory_items, Unset):
            inventory_items = []
            for inventory_items_item_data in self.inventory_items:
                inventory_items_item = inventory_items_item_data.to_dict()
                inventory_items.append(inventory_items_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory_items is not UNSET:
            field_dict["inventoryItems"] = inventory_items
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_item import InventoryItem

        d = dict(src_dict)
        _inventory_items = d.pop("inventoryItems", UNSET)
        inventory_items: list[InventoryItem] | Unset = UNSET
        if _inventory_items is not UNSET:
            inventory_items = []
            for inventory_items_item_data in _inventory_items:
                inventory_items_item = InventoryItem.from_dict(inventory_items_item_data)

                inventory_items.append(inventory_items_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_inventory_items_response = cls(
            inventory_items=inventory_items,
            next_page_token=next_page_token,
        )

        list_inventory_items_response.additional_properties = d
        return list_inventory_items_response

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
