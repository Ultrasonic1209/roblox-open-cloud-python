from __future__ import annotations

import datetime
from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="EntryVersion")


@_attrs_define
class EntryVersion:
    """The entry version object returned by the `List Entry Versions` method.

    Attributes:
        version (File | Unset): The version name of the qualifying entry.
        deleted (bool | Unset): Indicates whether the entry has been deleted. Default: False.
        content_length (float | Unset): The length of the content.
        created_time (datetime.datetime | Unset): The timestamp of when the version was created in the ISO time format.
        object_created_time (datetime.datetime | Unset): The timestamp of when the data store was created in the ISO
            time format.
    """

    version: File | Unset = UNSET
    deleted: bool | Unset = False
    content_length: float | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    object_created_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        version: FileTypes | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_tuple()

        deleted = self.deleted

        content_length = self.content_length

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        object_created_time: str | Unset = UNSET
        if not isinstance(self.object_created_time, Unset):
            object_created_time = self.object_created_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if content_length is not UNSET:
            field_dict["contentLength"] = content_length
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if object_created_time is not UNSET:
            field_dict["objectCreatedTime"] = object_created_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _version = d.pop("version", UNSET)
        version: File | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = File(payload=BytesIO(_version))

        deleted = d.pop("deleted", UNSET)

        content_length = d.pop("contentLength", UNSET)

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        _object_created_time = d.pop("objectCreatedTime", UNSET)
        object_created_time: datetime.datetime | Unset
        if isinstance(_object_created_time, Unset):
            object_created_time = UNSET
        else:
            object_created_time = datetime.datetime.fromisoformat(_object_created_time)

        entry_version = cls(
            version=version,
            deleted=deleted,
            content_length=content_length,
            created_time=created_time,
            object_created_time=object_created_time,
        )

        return entry_version
