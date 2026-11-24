from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem")


@_attrs_define
class UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem:
    """Represents a sorted map item name.

    Attributes:
        path (None | str | Unset): The resource path of the memory store hash map item.  Format:
            universes/{universe}/memory-store/hash-maps/{hash-map}/items/{hash-map-item}
        value (Any | Unset): Represents a dynamically typed value which can be either null, a number, a string, a
            boolean,
            a recursive struct value, or a list of values.
        etag (None | str | Unset): The server generated tag of an item.
        expire_time (datetime.datetime | None | Unset): The expiration time of an item.
        ttl (None | str | Unset): Gets or Sets Ttl
        id (None | str | Unset): The name of the item.
    """

    path: None | str | Unset = UNSET
    value: Any | Unset = UNSET
    etag: None | str | Unset = UNSET
    expire_time: datetime.datetime | None | Unset = UNSET
    ttl: None | str | Unset = UNSET
    id: None | str | Unset = UNSET

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

        ums_ums_service_models_open_cloud_open_cloud_hash_map_item = cls(
            path=path,
            value=value,
            etag=etag,
            expire_time=expire_time,
            ttl=ttl,
            id=id,
        )

        return ums_ums_service_models_open_cloud_open_cloud_hash_map_item
