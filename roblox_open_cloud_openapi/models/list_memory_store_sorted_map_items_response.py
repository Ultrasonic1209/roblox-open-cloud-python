from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_store_sorted_map_item import MemoryStoreSortedMapItem


T = TypeVar("T", bound="ListMemoryStoreSortedMapItemsResponse")


@_attrs_define
class ListMemoryStoreSortedMapItemsResponse:
    """A list of MemoryStoreSortedMapItems in the parent collection.

    Attributes:
        memory_store_sorted_map_items (list[MemoryStoreSortedMapItem] | Unset): The MemoryStoreSortedMapItems from the
            specified MemoryStoreSortedMap.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    memory_store_sorted_map_items: list[MemoryStoreSortedMapItem] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory_store_sorted_map_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.memory_store_sorted_map_items, Unset):
            memory_store_sorted_map_items = []
            for memory_store_sorted_map_items_item_data in self.memory_store_sorted_map_items:
                memory_store_sorted_map_items_item = memory_store_sorted_map_items_item_data.to_dict()
                memory_store_sorted_map_items.append(memory_store_sorted_map_items_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memory_store_sorted_map_items is not UNSET:
            field_dict["memoryStoreSortedMapItems"] = memory_store_sorted_map_items
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_store_sorted_map_item import MemoryStoreSortedMapItem

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _memory_store_sorted_map_items = d.pop("memoryStoreSortedMapItems", UNSET)
        memory_store_sorted_map_items: list[MemoryStoreSortedMapItem] | Unset = UNSET
        if _memory_store_sorted_map_items is not UNSET:
            memory_store_sorted_map_items = []
            for memory_store_sorted_map_items_item_data in _memory_store_sorted_map_items:
                memory_store_sorted_map_items_item = MemoryStoreSortedMapItem.from_dict(
                    memory_store_sorted_map_items_item_data
                )

                memory_store_sorted_map_items.append(memory_store_sorted_map_items_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_memory_store_sorted_map_items_response = cls(
            memory_store_sorted_map_items=memory_store_sorted_map_items,
            next_page_token=next_page_token,
        )

        list_memory_store_sorted_map_items_response.additional_properties = d
        return list_memory_store_sorted_map_items_response

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
