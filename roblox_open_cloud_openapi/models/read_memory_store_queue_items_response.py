from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_store_queue_item import MemoryStoreQueueItem


T = TypeVar("T", bound="ReadMemoryStoreQueueItemsResponse")


@_attrs_define
class ReadMemoryStoreQueueItemsResponse:
    """Returns the specified number of items at the front of the queue.

    Attributes:
        read_id (str | Unset): An identifier of the read operation

            This can be passed to `:discard` in order to mark the items as processed.
        items (list[MemoryStoreQueueItem] | Unset): The items read from the queue
    """

    read_id: str | Unset = UNSET
    items: list[MemoryStoreQueueItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read_id = self.read_id

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if read_id is not UNSET:
            field_dict["readId"] = read_id
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_store_queue_item import MemoryStoreQueueItem

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        read_id = d.pop("readId", UNSET)

        _items = d.pop("items", UNSET)
        items: list[MemoryStoreQueueItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = MemoryStoreQueueItem.from_dict(items_item_data)

                items.append(items_item)

        read_memory_store_queue_items_response = cls(
            read_id=read_id,
            items=items,
        )

        read_memory_store_queue_items_response.additional_properties = d
        return read_memory_store_queue_items_response

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
