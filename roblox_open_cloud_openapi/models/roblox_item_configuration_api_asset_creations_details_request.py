from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiAssetCreationsDetailsRequest")


@_attrs_define
class RobloxItemConfigurationApiAssetCreationsDetailsRequest:
    """
    Attributes:
        asset_ids (list[int] | Unset):
    """

    asset_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_ids: list[int] | Unset = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_ids is not UNSET:
            field_dict["AssetIds"] = asset_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        asset_ids = cast(list[int], d.pop("AssetIds", UNSET))

        roblox_item_configuration_api_asset_creations_details_request = cls(
            asset_ids=asset_ids,
        )

        return roblox_item_configuration_api_asset_creations_details_request
