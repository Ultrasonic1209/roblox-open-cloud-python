from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest")


@_attrs_define
class UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest:
    """Request to retrieve multiple hash map items by key.

    Attributes:
        keys (list[str] | None | Unset): The keys of the items to retrieve.
    """

    keys: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keys: list[str] | None | Unset
        if isinstance(self.keys, Unset):
            keys = UNSET
        elif isinstance(self.keys, list):
            keys = self.keys

        else:
            keys = self.keys

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keys_type_0 = cast(list[str], data)

                return keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keys = _parse_keys(d.pop("keys", UNSET))

        ums_ums_service_models_open_cloud_open_cloud_batch_get_hash_map_items_request = cls(
            keys=keys,
        )

        return ums_ums_service_models_open_cloud_open_cloud_batch_get_hash_map_items_request
