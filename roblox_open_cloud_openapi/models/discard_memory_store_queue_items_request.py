from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscardMemoryStoreQueueItemsRequest")


@_attrs_define
class DiscardMemoryStoreQueueItemsRequest:
    """Discards read items from the front of the queue.

    Attributes:
        read_id (str | Unset): The `readId` of the previous read operation for which to discard read
            items.
    """

    read_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read_id = self.read_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if read_id is not UNSET:
            field_dict["readId"] = read_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        read_id = d.pop("readId", UNSET)

        discard_memory_store_queue_items_request = cls(
            read_id=read_id,
        )

        discard_memory_store_queue_items_request.additional_properties = d
        return discard_memory_store_queue_items_request

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
