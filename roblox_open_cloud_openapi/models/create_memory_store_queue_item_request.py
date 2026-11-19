from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateMemoryStoreQueueItemRequest")


@_attrs_define
class CreateMemoryStoreQueueItemRequest:
    """Represents an item within a queue structure.

    Attributes:
        data (Any | Unset): The value of the queue item.
        ttl (None | str | Unset): The TTL for the item. Example: 3s.
        priority (float | Unset): The priority of the queue item.
    """

    data: Any | Unset = UNSET
    ttl: None | str | Unset = UNSET
    priority: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        ttl: None | str | Unset
        if isinstance(self.ttl, Unset):
            ttl = UNSET
        else:
            ttl = self.ttl

        priority = self.priority

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        def _parse_ttl(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ttl = _parse_ttl(d.pop("ttl", UNSET))

        priority = d.pop("priority", UNSET)

        create_memory_store_queue_item_request = cls(
            data=data,
            ttl=ttl,
            priority=priority,
        )

        return create_memory_store_queue_item_request
