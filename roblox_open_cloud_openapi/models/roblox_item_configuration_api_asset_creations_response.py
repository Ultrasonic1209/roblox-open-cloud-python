from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiAssetCreationsResponse")


@_attrs_define
class RobloxItemConfigurationApiAssetCreationsResponse:
    """Asset Status response model.

    Attributes:
        asset_id (int | Unset): The asset Id.
        name (str | Unset): The asset name.
    """

    asset_id: int | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_id = d.pop("assetId", UNSET)

        name = d.pop("name", UNSET)

        roblox_item_configuration_api_asset_creations_response = cls(
            asset_id=asset_id,
            name=name,
        )

        return roblox_item_configuration_api_asset_creations_response
