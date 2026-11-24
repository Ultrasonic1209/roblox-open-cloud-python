from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ums_ums_service_models_open_cloud_open_cloud_hash_map_item import (
        UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem,
    )


T = TypeVar("T", bound="UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse")


@_attrs_define
class UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse:
    """The hash map items retrieved for the requested keys. Keys that are not
    found are omitted from the response.

        Attributes:
            items (list[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem] | None | Unset): The retrieved hash map items.
    """

    items: list[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem] | None | Unset = UNSET

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

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

        ums_ums_service_models_open_cloud_open_cloud_batch_get_hash_map_items_response = cls(
            items=items,
        )

        return ums_ums_service_models_open_cloud_open_cloud_batch_get_hash_map_items_response
