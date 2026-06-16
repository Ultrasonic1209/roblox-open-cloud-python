from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_asset_delivery_api_asset_metadata_metadata_type import (
    RobloxAssetDeliveryApiAssetMetadataMetadataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAssetDeliveryApiAssetMetadata")


@_attrs_define
class RobloxAssetDeliveryApiAssetMetadata:
    """An asset piece of metadata.

    Attributes:
        metadata_type (RobloxAssetDeliveryApiAssetMetadataMetadataType | Unset): Asset metadata type.
            ['UncompressedSize' = 1]
        value (str | Unset):
    """

    metadata_type: RobloxAssetDeliveryApiAssetMetadataMetadataType | Unset = UNSET
    value: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metadata_type: int | Unset = UNSET
        if not isinstance(self.metadata_type, Unset):
            metadata_type = self.metadata_type.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if metadata_type is not UNSET:
            field_dict["metadataType"] = metadata_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _metadata_type = d.pop("metadataType", UNSET)
        metadata_type: RobloxAssetDeliveryApiAssetMetadataMetadataType | Unset
        if isinstance(_metadata_type, Unset):
            metadata_type = UNSET
        else:
            metadata_type = RobloxAssetDeliveryApiAssetMetadataMetadataType(_metadata_type)

        value = d.pop("value", UNSET)

        roblox_asset_delivery_api_asset_metadata = cls(
            metadata_type=metadata_type,
            value=value,
        )

        return roblox_asset_delivery_api_asset_metadata
