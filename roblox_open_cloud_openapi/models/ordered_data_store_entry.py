from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderedDataStoreEntry")


@_attrs_define
class OrderedDataStoreEntry:
    """A key-value entry in an ordered data store.

    Attributes:
        path (str | Unset): The resource path of the ordered data store entry.

            Format:
            `universes/{universe_id}/ordered-data-
            stores/{ordered_data_store_id}/scopes/{ordered_data_store_scope_id}/entries/{ordered_data_store_entry_id}`
            Example: universes/123/ordered-data-stores/some-ordered-data-store-id/scopes/some-ordered-data-store-scope-
            id/entries/some-ordered-data-store-entry-id.
        value (float | Unset): The value of the entry.

            Always rounded to the nearest integer.
        id (str | Unset): The name of the entry.
    """

    path: str | Unset = UNSET
    value: float | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        value = self.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if value is not UNSET:
            field_dict["value"] = value
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        value = d.pop("value", UNSET)

        id = d.pop("id", UNSET)

        ordered_data_store_entry = cls(
            path=path,
            value=value,
            id=id,
        )

        ordered_data_store_entry.additional_properties = d
        return ordered_data_store_entry

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
