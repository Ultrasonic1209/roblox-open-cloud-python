from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryStoreQueueItem")


@_attrs_define
class MemoryStoreQueueItem:
    """Represents an item within a queue structure.

    Attributes:
        path (None | str | Unset): The resource path of the memory store queue item.

            Format:
            `cloud/v2/universes/{universe_id}/memory-
            store/queues/{memory_store_queue_id}/items/{memory_store_queue_item_id}` Example: cloud/v2/universes/123/memory-
            store/queues/some-memory-store-queue-id/items/some-memory-store-queue-item-id.
        data (Any | Unset): The value of the queue item.
        priority (float | Unset): The priority of the queue item.
        expire_time (datetime.datetime | Unset): The expiration time of the item. Example: 2023-07-05T12:34:56Z.
        ttl (None | str | Unset): The TTL for the item. Example: 3s.
    """

    path: None | str | Unset = UNSET
    data: Any | Unset = UNSET
    priority: float | Unset = UNSET
    expire_time: datetime.datetime | Unset = UNSET
    ttl: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        data = self.data

        priority = self.priority

        expire_time: str | Unset = UNSET
        if not isinstance(self.expire_time, Unset):
            expire_time = self.expire_time.isoformat()

        ttl: None | str | Unset
        if isinstance(self.ttl, Unset):
            ttl = UNSET
        else:
            ttl = self.ttl

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if data is not UNSET:
            field_dict["data"] = data
        if priority is not UNSET:
            field_dict["priority"] = priority
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if ttl is not UNSET:
            field_dict["ttl"] = ttl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        data = d.pop("data", UNSET)

        priority = d.pop("priority", UNSET)

        _expire_time = d.pop("expireTime", UNSET)
        expire_time: datetime.datetime | Unset
        if isinstance(_expire_time, Unset):
            expire_time = UNSET
        else:
            expire_time = datetime.datetime.fromisoformat(_expire_time)

        def _parse_ttl(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ttl = _parse_ttl(d.pop("ttl", UNSET))

        memory_store_queue_item = cls(
            path=path,
            data=data,
            priority=priority,
            expire_time=expire_time,
            ttl=ttl,
        )

        return memory_store_queue_item
