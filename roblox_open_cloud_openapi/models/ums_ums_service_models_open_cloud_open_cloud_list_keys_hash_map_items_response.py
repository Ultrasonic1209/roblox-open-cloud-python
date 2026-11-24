from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ums_ums_service_models_open_cloud_open_cloud_hash_map_item import (
        UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem,
    )


T = TypeVar("T", bound="UmsUmsServiceModelsOpenCloudOpenCloudListKeysHashMapItemsResponse")


@_attrs_define
class UmsUmsServiceModelsOpenCloudOpenCloudListKeysHashMapItemsResponse:
    """A list of MemoryStoreHashMapItems in the parent collection.

    Attributes:
        items (list[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem] | None | Unset): The MemoryStoreHashMapItems from
            the specified MemoryStoreHashMap.
        next_page_token (None | str | Unset): A token that you can send as a pageToken parameter to retrieve the next
            page.
            If this field is omitted, there are no subsequent pages.
    """

    items: list[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem] | None | Unset = UNSET
    next_page_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ums_ums_service_models_open_cloud_open_cloud_hash_map_item import (
            UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_items(data: object) -> list[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem.from_dict(
                        items_type_0_item_data
                    )

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        ums_ums_service_models_open_cloud_open_cloud_list_keys_hash_map_items_response = cls(
            items=items,
            next_page_token=next_page_token,
        )

        return ums_ums_service_models_open_cloud_open_cloud_list_keys_hash_map_items_response
