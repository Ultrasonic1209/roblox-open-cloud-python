from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscardMemoryStoreQueueItemsRequest")


@_attrs_define
class DiscardMemoryStoreQueueItemsRequest:
    """Discards read items from the front of the queue.

    Attributes:
        read_id (None | str | Unset): The `id` of the previous read operation for which to discard read
            items.
    """

    read_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        read_id: None | str | Unset
        if isinstance(self.read_id, Unset):
            read_id = UNSET
        else:
            read_id = self.read_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if read_id is not UNSET:
            field_dict["readId"] = read_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_read_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        read_id = _parse_read_id(d.pop("readId", UNSET))

        discard_memory_store_queue_items_request = cls(
            read_id=read_id,
        )

        return discard_memory_store_queue_items_request
