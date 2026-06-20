from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_store_entry import DataStoreEntry


T = TypeVar("T", bound="ListDataStoreEntryRevisionsResponse")


@_attrs_define
class ListDataStoreEntryRevisionsResponse:
    """A list of revisions of a data store entry.

    Attributes:
        data_store_entries (list[DataStoreEntry] | Unset): The revisions of the data_store_entry.
        next_page_token (str | Unset): A token that you send as a `pageToken` parameter to retrieve the next page.
            If this field is omitted, there are no subsequent pages.
    """

    data_store_entries: list[DataStoreEntry] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_store_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_store_entries, Unset):
            data_store_entries = []
            for data_store_entries_item_data in self.data_store_entries:
                data_store_entries_item = data_store_entries_item_data.to_dict()
                data_store_entries.append(data_store_entries_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_store_entries is not UNSET:
            field_dict["dataStoreEntries"] = data_store_entries
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_store_entry import DataStoreEntry

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _data_store_entries = d.pop("dataStoreEntries", UNSET)
        data_store_entries: list[DataStoreEntry] | Unset = UNSET
        if _data_store_entries is not UNSET:
            data_store_entries = []
            for data_store_entries_item_data in _data_store_entries:
                data_store_entries_item = DataStoreEntry.from_dict(data_store_entries_item_data)

                data_store_entries.append(data_store_entries_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_data_store_entry_revisions_response = cls(
            data_store_entries=data_store_entries,
            next_page_token=next_page_token,
        )

        list_data_store_entry_revisions_response.additional_properties = d
        return list_data_store_entry_revisions_response

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
