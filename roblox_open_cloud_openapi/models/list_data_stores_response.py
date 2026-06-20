from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_store import DataStore


T = TypeVar("T", bound="ListDataStoresResponse")


@_attrs_define
class ListDataStoresResponse:
    """A list of DataStores in the parent collection.

    Attributes:
        data_stores (list[DataStore] | Unset): The DataStores from the specified Universe.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    data_stores: list[DataStore] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_stores: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_stores, Unset):
            data_stores = []
            for data_stores_item_data in self.data_stores:
                data_stores_item = data_stores_item_data.to_dict()
                data_stores.append(data_stores_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_stores is not UNSET:
            field_dict["dataStores"] = data_stores
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_store import DataStore

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _data_stores = d.pop("dataStores", UNSET)
        data_stores: list[DataStore] | Unset = UNSET
        if _data_stores is not UNSET:
            data_stores = []
            for data_stores_item_data in _data_stores:
                data_stores_item = DataStore.from_dict(data_stores_item_data)

                data_stores.append(data_stores_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_data_stores_response = cls(
            data_stores=data_stores,
            next_page_token=next_page_token,
        )

        list_data_stores_response.additional_properties = d
        return list_data_stores_response

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
