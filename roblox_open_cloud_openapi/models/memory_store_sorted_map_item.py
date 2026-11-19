from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryStoreSortedMapItem")


@_attrs_define
class MemoryStoreSortedMapItem:
    """Represents an item within a sorted map structure.

    Attributes:
        path (None | str | Unset): The resource path of the memory store sorted map item.

            Format:
            `cloud/v2/universes/{universe_id}/memory-store/sorted-
            maps/{memory_store_sorted_map_id}/items/{memory_store_sorted_map_item_id}` Example:
            cloud/v2/universes/123/memory-store/sorted-maps/some-memory-store-sorted-map-id/items/some-memory-store-sorted-
            map-item-id.
        value (Any | Unset): The value of the item.
        etag (None | str | Unset): The server generated tag of an item.

            When updating an item, if `etag` is provided, the update only succeeds if
            it matches the current tag of the item.
        expire_time (datetime.datetime | None | Unset): The expiration time of the item. Example: 2023-07-05T12:34:56Z.
        ttl (None | str | Unset): Required on create and update. It must be a number ending in `s`, greater than 0 and
            at most `3888000s`.
            The response reports expiration as `expireTime`, not `ttl`. Example: 3s.
        id (None | str | Unset): The name of the item.
        string_sort_key (None | str | Unset): The item will be sorted lexicographically according to this string.
        numeric_sort_key (float | None | Unset): The item will be sorted according to this number.
    """

    path: None | str | Unset = UNSET
    value: Any | Unset = UNSET
    etag: None | str | Unset = UNSET
    expire_time: datetime.datetime | None | Unset = UNSET
    ttl: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    string_sort_key: None | str | Unset = UNSET
    numeric_sort_key: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        value = self.value

        etag: None | str | Unset
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

        expire_time: None | str | Unset
        if isinstance(self.expire_time, Unset):
            expire_time = UNSET
        elif isinstance(self.expire_time, datetime.datetime):
            expire_time = self.expire_time.isoformat()
        else:
            expire_time = self.expire_time

        ttl: None | str | Unset
        if isinstance(self.ttl, Unset):
            ttl = UNSET
        else:
            ttl = self.ttl

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        string_sort_key: None | str | Unset
        if isinstance(self.string_sort_key, Unset):
            string_sort_key = UNSET
        else:
            string_sort_key = self.string_sort_key

        numeric_sort_key: float | None | Unset
        if isinstance(self.numeric_sort_key, Unset):
            numeric_sort_key = UNSET
        else:
            numeric_sort_key = self.numeric_sort_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if value is not UNSET:
            field_dict["value"] = value
        if etag is not UNSET:
            field_dict["etag"] = etag
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
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

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        value = d.pop("value", UNSET)

        def _parse_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        etag = _parse_etag(d.pop("etag", UNSET))

        def _parse_expire_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expire_time_type_0 = datetime.datetime.fromisoformat(data)

                return expire_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expire_time = _parse_expire_time(d.pop("expireTime", UNSET))

        def _parse_ttl(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ttl = _parse_ttl(d.pop("ttl", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_string_sort_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        string_sort_key = _parse_string_sort_key(d.pop("stringSortKey", UNSET))

        def _parse_numeric_sort_key(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        numeric_sort_key = _parse_numeric_sort_key(d.pop("numericSortKey", UNSET))

        memory_store_sorted_map_item = cls(
            path=path,
            value=value,
            etag=etag,
            expire_time=expire_time,
            ttl=ttl,
            id=id,
            string_sort_key=string_sort_key,
            numeric_sort_key=numeric_sort_key,
        )

        return memory_store_sorted_map_item
