from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ordered_data_store_entry import OrderedDataStoreEntry


T = TypeVar("T", bound="ListOrderedDataStoreEntriesResponse")


@_attrs_define
class ListOrderedDataStoreEntriesResponse:
    """A list of OrderedDataStoreEntries in the parent collection.

    Attributes:
        ordered_data_store_entries (list[OrderedDataStoreEntry] | Unset): The OrderedDataStoreEntries from the specified
            OrderedDataStoreScope.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    ordered_data_store_entries: list[OrderedDataStoreEntry] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ordered_data_store_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ordered_data_store_entries, Unset):
            ordered_data_store_entries = []
            for ordered_data_store_entries_item_data in self.ordered_data_store_entries:
                ordered_data_store_entries_item = ordered_data_store_entries_item_data.to_dict()
                ordered_data_store_entries.append(ordered_data_store_entries_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordered_data_store_entries is not UNSET:
            field_dict["orderedDataStoreEntries"] = ordered_data_store_entries
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ordered_data_store_entry import OrderedDataStoreEntry

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _ordered_data_store_entries = d.pop("orderedDataStoreEntries", UNSET)
        ordered_data_store_entries: list[OrderedDataStoreEntry] | Unset = UNSET
        if _ordered_data_store_entries is not UNSET:
            ordered_data_store_entries = []
            for ordered_data_store_entries_item_data in _ordered_data_store_entries:
                ordered_data_store_entries_item = OrderedDataStoreEntry.from_dict(ordered_data_store_entries_item_data)

                ordered_data_store_entries.append(ordered_data_store_entries_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_ordered_data_store_entries_response = cls(
            ordered_data_store_entries=ordered_data_store_entries,
            next_page_token=next_page_token,
        )

        list_ordered_data_store_entries_response.additional_properties = d
        return list_ordered_data_store_entries_response

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
