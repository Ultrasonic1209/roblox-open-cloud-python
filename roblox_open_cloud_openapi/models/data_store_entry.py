from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_store_entry_state import DataStoreEntryState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_store_entry_attributes import DataStoreEntryAttributes


T = TypeVar("T", bound="DataStoreEntry")


@_attrs_define
class DataStoreEntry:
    """A key-value entry in a data store.

    Attributes:
        path (str | Unset): The resource path of the data store entry.

            Formats:
            * `universes/{universe_id}/data-stores/{data_store_id}/entries/{data_store_entry_id}`
            * `universes/{universe_id}/data-
            stores/{data_store_id}/scopes/{data_store_scope_id}/entries/{data_store_entry_id}` Example: universes/123/data-
            stores/some-data-store/entries/some-data-store-entry.
        create_time (datetime.datetime | Unset): The timestamp when the data store entry was created. Example:
            2023-07-05T12:34:56Z.
        revision_id (str | Unset): The revision ID of the data store entry.

            A new revision is committed whenever the data store entry is changed in any
            way.

            The format is an arbitrary string.
            Example: "foo"
        revision_create_time (datetime.datetime | Unset): The timestamp when the revision was created. Example:
            2023-07-05T12:34:56Z.
        state (DataStoreEntryState | Unset): The state of the data store entry.

            Possible values:

              | Value | Description |
              | --- | --- |
              | STATE_UNSPECIFIED | The default value. This value is used if the state is omitted. |
              | ACTIVE | The data store entry is active.  The default state of a newly created data store entry. |
              | DELETED | The data store entry is deleted.  At some point in the future, it will be permanently deleted. |
            Example: STATE_UNSPECIFIED.
        etag (str | Unset): This checksum is computed by the server based on the value of other
            fields, and may be sent on update and delete requests (and potentially
            on certain custom methods) to ensure the client has an up-to-date
            value before proceeding.
        value (Any | Unset): Represents a dynamically typed value which can be either null, a number, a string, a
            boolean, a recursive struct value, or a list of values.
        id (str | Unset): The resource ID of the entry.

            This matches the last segment of the resource path, and is provided
            only for convenience.
        users (list[str] | Unset): Users associated with the entry.
        attributes (DataStoreEntryAttributes | Unset): An arbitrary set of attributes associated with the entry.
    """

    path: str | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    revision_id: str | Unset = UNSET
    revision_create_time: datetime.datetime | Unset = UNSET
    state: DataStoreEntryState | Unset = UNSET
    etag: str | Unset = UNSET
    value: Any | Unset = UNSET
    id: str | Unset = UNSET
    users: list[str] | Unset = UNSET
    attributes: DataStoreEntryAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        revision_id = self.revision_id

        revision_create_time: str | Unset = UNSET
        if not isinstance(self.revision_create_time, Unset):
            revision_create_time = self.revision_create_time.isoformat()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        etag = self.etag

        value = self.value

        id = self.id

        users: list[str] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if revision_create_time is not UNSET:
            field_dict["revisionCreateTime"] = revision_create_time
        if state is not UNSET:
            field_dict["state"] = state
        if etag is not UNSET:
            field_dict["etag"] = etag
        if value is not UNSET:
            field_dict["value"] = value
        if id is not UNSET:
            field_dict["id"] = id
        if users is not UNSET:
            field_dict["users"] = users
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_store_entry_attributes import DataStoreEntryAttributes

        d = dict(src_dict)
        path = d.pop("path", UNSET)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        revision_id = d.pop("revisionId", UNSET)

        _revision_create_time = d.pop("revisionCreateTime", UNSET)
        revision_create_time: datetime.datetime | Unset
        if isinstance(_revision_create_time, Unset):
            revision_create_time = UNSET
        else:
            revision_create_time = datetime.datetime.fromisoformat(_revision_create_time)

        _state = d.pop("state", UNSET)
        state: DataStoreEntryState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DataStoreEntryState(_state)

        etag = d.pop("etag", UNSET)

        value = d.pop("value", UNSET)

        id = d.pop("id", UNSET)

        users = cast(list[str], d.pop("users", UNSET))

        _attributes = d.pop("attributes", UNSET)
        attributes: DataStoreEntryAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = DataStoreEntryAttributes.from_dict(_attributes)

        data_store_entry = cls(
            path=path,
            create_time=create_time,
            revision_id=revision_id,
            revision_create_time=revision_create_time,
            state=state,
            etag=etag,
            value=value,
            id=id,
            users=users,
            attributes=attributes,
        )

        data_store_entry.additional_properties = d
        return data_store_entry

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
