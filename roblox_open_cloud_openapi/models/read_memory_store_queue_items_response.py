from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_store_queue_item import MemoryStoreQueueItem


T = TypeVar("T", bound="ReadMemoryStoreQueueItemsResponse")


@_attrs_define
class ReadMemoryStoreQueueItemsResponse:
    """Returns the specified number of items at the front of the queue.

    Attributes:
        queue_items (list[MemoryStoreQueueItem] | None | Unset): The items read from the queue
        id (None | str | Unset): An identifier of the read operation

            This can be passed to `:discard` as `readId` in order to mark the items as processed.
    """

    queue_items: list[MemoryStoreQueueItem] | None | Unset = UNSET
    id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        queue_items: list[dict[str, Any]] | None | Unset
        if isinstance(self.queue_items, Unset):
            queue_items = UNSET
        elif isinstance(self.queue_items, list):
            queue_items = []
            for queue_items_type_0_item_data in self.queue_items:
                queue_items_type_0_item = queue_items_type_0_item_data.to_dict()
                queue_items.append(queue_items_type_0_item)

        else:
            queue_items = self.queue_items

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if queue_items is not UNSET:
            field_dict["queueItems"] = queue_items
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_store_queue_item import MemoryStoreQueueItem  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_queue_items(data: object) -> list[MemoryStoreQueueItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                queue_items_type_0 = []
                _queue_items_type_0 = data
                for queue_items_type_0_item_data in _queue_items_type_0:
                    queue_items_type_0_item = MemoryStoreQueueItem.from_dict(queue_items_type_0_item_data)

                    queue_items_type_0.append(queue_items_type_0_item)

                return queue_items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MemoryStoreQueueItem] | None | Unset, data)

        queue_items = _parse_queue_items(d.pop("queueItems", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        read_memory_store_queue_items_response = cls(
            queue_items=queue_items,
            id=id,
        )

        return read_memory_store_queue_items_response
