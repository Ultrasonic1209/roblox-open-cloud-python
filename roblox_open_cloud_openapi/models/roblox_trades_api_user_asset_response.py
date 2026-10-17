from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_trades_api_user_asset_response_membership_type import (
    RobloxTradesApiUserAssetResponseMembershipType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiUserAssetResponse")


@_attrs_define
class RobloxTradesApiUserAssetResponse:
    """A model containing information about a UserAsset.

    Attributes:
        id (int | Unset): The user asset id
        serial_number (int | Unset): The serial number of the user asset
        asset_id (int | Unset): The asset id of the user asset
        name (str | Unset): The asset name of the asset
        recent_average_price (int | Unset): The recent average price of the asset
        original_price (int | Unset): The original price of the asset
        asset_stock (int | Unset): The asset stock.
        membership_type (RobloxTradesApiUserAssetResponseMembershipType | Unset): The minimum MembershipType required to
            own the userAsset. ['None' = 0, 'BC' = 1, 'TBC' = 2, 'OBC' = 3, 'RobloxPremium' = 4]
    """

    id: int | Unset = UNSET
    serial_number: int | Unset = UNSET
    asset_id: int | Unset = UNSET
    name: str | Unset = UNSET
    recent_average_price: int | Unset = UNSET
    original_price: int | Unset = UNSET
    asset_stock: int | Unset = UNSET
    membership_type: RobloxTradesApiUserAssetResponseMembershipType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        serial_number = self.serial_number

        asset_id = self.asset_id

        name = self.name

        recent_average_price = self.recent_average_price

        original_price = self.original_price

        asset_stock = self.asset_stock

        membership_type: int | Unset = UNSET
        if not isinstance(self.membership_type, Unset):
            membership_type = self.membership_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if name is not UNSET:
            field_dict["name"] = name
        if recent_average_price is not UNSET:
            field_dict["recentAveragePrice"] = recent_average_price
        if original_price is not UNSET:
            field_dict["originalPrice"] = original_price
        if asset_stock is not UNSET:
            field_dict["assetStock"] = asset_stock
        if membership_type is not UNSET:
            field_dict["membershipType"] = membership_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        asset_id = d.pop("assetId", UNSET)

        name = d.pop("name", UNSET)

        recent_average_price = d.pop("recentAveragePrice", UNSET)

        original_price = d.pop("originalPrice", UNSET)

        asset_stock = d.pop("assetStock", UNSET)

        _membership_type = d.pop("membershipType", UNSET)
        membership_type: RobloxTradesApiUserAssetResponseMembershipType | Unset
        if isinstance(_membership_type, Unset):
            membership_type = UNSET
        else:
            membership_type = RobloxTradesApiUserAssetResponseMembershipType(_membership_type)

        roblox_trades_api_user_asset_response = cls(
            id=id,
            serial_number=serial_number,
            asset_id=asset_id,
            name=name,
            recent_average_price=recent_average_price,
            original_price=original_price,
            asset_stock=asset_stock,
            membership_type=membership_type,
        )

        return roblox_trades_api_user_asset_response
