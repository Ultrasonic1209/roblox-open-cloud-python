from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.roblox_2_assetdelivery_v3_asset_request_item import Roblox2AssetdeliveryV3AssetRequestItem


T = TypeVar("T", bound="Roblox2AssetdeliveryV3V3BatchRequest")


@_attrs_define
class Roblox2AssetdeliveryV3V3BatchRequest:
    """
    Attributes:
        assets (list[Roblox2AssetdeliveryV3AssetRequestItem]):
    """

    assets: list[Roblox2AssetdeliveryV3AssetRequestItem]

    def to_dict(self) -> dict[str, Any]:
        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assets": assets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_2_assetdelivery_v3_asset_request_item import Roblox2AssetdeliveryV3AssetRequestItem  # noqa: PLC0415

        d = dict(src_dict)
        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = Roblox2AssetdeliveryV3AssetRequestItem.from_dict(assets_item_data)

            assets.append(assets_item)

        roblox_2_assetdelivery_v3v3_batch_request = cls(
            assets=assets,
        )

        return roblox_2_assetdelivery_v3v3_batch_request
