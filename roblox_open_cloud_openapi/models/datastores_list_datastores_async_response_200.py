from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ocv1_data_stores_data_store import OCV1DataStoresDataStore


T = TypeVar("T", bound="DatastoresListDatastoresAsyncResponse200")


@_attrs_define
class DatastoresListDatastoresAsyncResponse200:
    """
    Example:
        {
              "datastores": [
                {
                  "name": "PlayerInventory",
                  "createdTime": "2022-02-18T22:38:59.9244932Z"
                },
                {
                  "name": "PlayerExperience",
                  "createdTime": "2022-02-18T23:00:10.4773508Z"
                },
                {
                  "name": "PlayerWeapons",
                  "createdTime": "2022-02-18T23:00:22.3725681Z"
                },
                {
                  "name": "PlayerArmor",
                  "createdTime": "2022-02-18T22:59:33.8472882Z"
                },
                {
                  "name": "PlayerHP",
                  "createdTime": "2022-02-18T22:58:47.6904028Z"
                }
              ],
              "nextPageCursor": "..."
            }

    Attributes:
        data (list[OCV1DataStoresDataStore] | Unset): An array of data stores in the target experience.
        next_page_cursor (None | str | Unset): Indicates that there is more data available in the requested result set.
    """

    data: list[OCV1DataStoresDataStore] | Unset = UNSET
    next_page_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        next_page_cursor: None | str | Unset
        if isinstance(self.next_page_cursor, Unset):
            next_page_cursor = UNSET
        else:
            next_page_cursor = self.next_page_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ocv1_data_stores_data_store import OCV1DataStoresDataStore

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[OCV1DataStoresDataStore] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = OCV1DataStoresDataStore.from_dict(data_item_data)

                data.append(data_item)

        def _parse_next_page_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_cursor = _parse_next_page_cursor(d.pop("nextPageCursor", UNSET))

        datastores_list_datastores_async_response_200 = cls(
            data=data,
            next_page_cursor=next_page_cursor,
        )

        datastores_list_datastores_async_response_200.additional_properties = d
        return datastores_list_datastores_async_response_200

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
