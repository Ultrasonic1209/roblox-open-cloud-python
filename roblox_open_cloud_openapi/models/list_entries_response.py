from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entry import Entry


T = TypeVar("T", bound="ListEntriesResponse")


@_attrs_define
class ListEntriesResponse:
    """A list of Entries in the parent collection.

    Attributes:
        entries (list[Entry] | Unset): The Entries from the specified Scope.
        next_page_token (str | Unset): A token, which can be sent as `page_token` to retrieve the next page. If this
            field is omitted, there are no subsequent pages.
    """

    entries: list[Entry] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entry import Entry

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _entries = d.pop("entries", UNSET)
        entries: list[Entry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = Entry.from_dict(entries_item_data)

                entries.append(entries_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_entries_response = cls(
            entries=entries,
            next_page_token=next_page_token,
        )

        list_entries_response.additional_properties = d
        return list_entries_response

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
