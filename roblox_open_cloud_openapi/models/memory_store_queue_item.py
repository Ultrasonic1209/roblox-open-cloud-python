from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryStoreQueueItem")


@_attrs_define
class MemoryStoreQueueItem:
    """Represents an item within a queue structure.

    Attributes:
        path (str | Unset): The resource path of the memory store queue item.

            Format:
            `cloud/v2/universes/{universe_id}/memory-
            store/queues/{memory_store_queue_id}/items/{memory_store_queue_item_id}` Example: cloud/v2/universes/123/memory-
            store/queues/some-memory-store-queue-id/items/some-memory-store-queue-item-id.
        data (Any | Unset): Represents a dynamically typed value which can be either null, a number, a string, a
            boolean, a recursive struct value, or a list of values.
        priority (float | Unset): The priority of the queue item.
        ttl (str | Unset): The TTL for the item. Example: 3s.
        expire_time (datetime.datetime | Unset): The expiration time of the item. Example: 2023-07-05T12:34:56Z.
        id (str | Unset): The name of the item.
    """

    path: str | Unset = UNSET
    data: Any | Unset = UNSET
    priority: float | Unset = UNSET
    ttl: str | Unset = UNSET
    expire_time: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        data = self.data

        priority = self.priority

        ttl = self.ttl

        expire_time: str | Unset = UNSET
        if not isinstance(self.expire_time, Unset):
            expire_time = self.expire_time.isoformat()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if data is not UNSET:
            field_dict["data"] = data
        if priority is not UNSET:
            field_dict["priority"] = priority
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        data = d.pop("data", UNSET)

        priority = d.pop("priority", UNSET)

        ttl = d.pop("ttl", UNSET)

        _expire_time = d.pop("expireTime", UNSET)
        expire_time: datetime.datetime | Unset
        if isinstance(_expire_time, Unset):
            expire_time = UNSET
        else:
            expire_time = datetime.datetime.fromisoformat(_expire_time)

        id = d.pop("id", UNSET)

        memory_store_queue_item = cls(
            path=path,
            data=data,
            priority=priority,
            ttl=ttl,
            expire_time=expire_time,
            id=id,
        )

        memory_store_queue_item.additional_properties = d
        return memory_store_queue_item

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
