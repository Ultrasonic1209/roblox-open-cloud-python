from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_store_state import DataStoreState
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataStore")


@_attrs_define
class DataStore:
    """Represents a data store.

    Attributes:
        path (str | Unset): The resource path of the data store.

            Format: `universes/{universe_id}/data-stores/{data_store_id}` Example: universes/123/data-stores/some-data-
            store.
        create_time (datetime.datetime | Unset): The timestamp when the data store was created. Example:
            2023-07-05T12:34:56Z.
        expire_time (datetime.datetime | Unset): The timestamp when the data store will expire (or did expire).

            This field is set when the data store is soft-deleted and indicates
            when it will be permanently removed. Example: 2023-07-05T12:34:56Z.
        state (DataStoreState | Unset): The state of the data store.

            Possible values:

              | Value | Description |
              | --- | --- |
              | STATE_UNSPECIFIED | The default value. This value is used if the state is omitted. |
              | ACTIVE | The data store is active. |
              | DELETED | The data store is deleted.  After the expiration time passes, it will be permanently deleted. |
            Example: STATE_UNSPECIFIED.
        id (str | Unset): The ID of the data store. Matches the last segment of the path.
    """

    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    expire_time: datetime.datetime | Unset = UNSET
    state: DataStoreState | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        expire_time: str | Unset = UNSET
        if not isinstance(self.expire_time, Unset):
            expire_time = self.expire_time.isoformat()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if state is not UNSET:
            field_dict["state"] = state
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _expire_time = d.pop("expireTime", UNSET)
        expire_time: datetime.datetime | Unset
        if isinstance(_expire_time, Unset):
            expire_time = UNSET
        else:
            expire_time = datetime.datetime.fromisoformat(_expire_time)

        _state = d.pop("state", UNSET)
        state: DataStoreState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DataStoreState(_state)

        id = d.pop("id", UNSET)

        data_store = cls(
            path=path,
            create_time=create_time,
            expire_time=expire_time,
            state=state,
            id=id,
        )

        data_store.additional_properties = d
        return data_store

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
