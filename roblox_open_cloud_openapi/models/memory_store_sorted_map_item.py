from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryStoreSortedMapItem")


@_attrs_define
class MemoryStoreSortedMapItem:
    """Represents an item within a sorted map structure.

    Attributes:
        path (str | Unset): The resource path of the memory store sorted map item.

            Format:
            `cloud/v2/universes/{universe_id}/memory-store/sorted-
            maps/{memory_store_sorted_map_id}/items/{memory_store_sorted_map_item_id}` Example:
            cloud/v2/universes/123/memory-store/sorted-maps/some-memory-store-sorted-map-id/items/some-memory-store-sorted-
            map-item-id.
        value (Any | Unset): Represents a dynamically typed value which can be either null, a number, a string, a
            boolean, a recursive struct value, or a list of values.
        etag (str | Unset): The server generated tag of an item.
        ttl (str | Unset): The TTL for the item. Example: 3s.
        expire_time (datetime.datetime | Unset): The expiration time of the item. Example: 2023-07-05T12:34:56Z.
        id (str | Unset): The name of the item.
        string_sort_key (str | Unset): The item will be sorted lexicographically according to this string.
        numeric_sort_key (float | Unset): The item will be sorted according to this number.
    """

    path: str | Unset = UNSET
    value: Any | Unset = UNSET
    etag: str | Unset = UNSET
    ttl: str | Unset = UNSET
    expire_time: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    string_sort_key: str | Unset = UNSET
    numeric_sort_key: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        value = self.value

        etag = self.etag

        ttl = self.ttl

        expire_time: str | Unset = UNSET
        if not isinstance(self.expire_time, Unset):
            expire_time = self.expire_time.isoformat()

        id = self.id

        string_sort_key = self.string_sort_key

        numeric_sort_key = self.numeric_sort_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if value is not UNSET:
            field_dict["value"] = value
        if etag is not UNSET:
            field_dict["etag"] = etag
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if id is not UNSET:
            field_dict["id"] = id
        if string_sort_key is not UNSET:
            field_dict["stringSortKey"] = string_sort_key
        if numeric_sort_key is not UNSET:
            field_dict["numericSortKey"] = numeric_sort_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        value = d.pop("value", UNSET)

        etag = d.pop("etag", UNSET)

        ttl = d.pop("ttl", UNSET)

        _expire_time = d.pop("expireTime", UNSET)
        expire_time: datetime.datetime | Unset
        if isinstance(_expire_time, Unset):
            expire_time = UNSET
        else:
            expire_time = datetime.datetime.fromisoformat(_expire_time)

        id = d.pop("id", UNSET)

        string_sort_key = d.pop("stringSortKey", UNSET)

        numeric_sort_key = d.pop("numericSortKey", UNSET)

        memory_store_sorted_map_item = cls(
            path=path,
            value=value,
            etag=etag,
            ttl=ttl,
            expire_time=expire_time,
            id=id,
            string_sort_key=string_sort_key,
            numeric_sort_key=numeric_sort_key,
        )

        memory_store_sorted_map_item.additional_properties = d
        return memory_store_sorted_map_item

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
