from __future__ import annotations

import datetime
from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="OCV1DataStoresDataStore")


@_attrs_define
class OCV1DataStoresDataStore:
    """The data store object with its name and created time.

    Attributes:
        name (File | Unset): The name of your data store.
        created_time (datetime.datetime | None | Unset): The timestamp of when the data store was created in the ISO
            time format.
    """

    name: File | Unset = UNSET
    created_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: FileTypes | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_tuple()

        created_time: None | str | Unset
        if isinstance(self.created_time, Unset):
            created_time = UNSET
        elif isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: File | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = File(payload=BytesIO(_name))

        def _parse_created_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_type_0 = datetime.datetime.fromisoformat(data)

                return created_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_time = _parse_created_time(d.pop("createdTime", UNSET))

        ocv1_data_stores_data_store = cls(
            name=name,
            created_time=created_time,
        )

        return ocv1_data_stores_data_store
