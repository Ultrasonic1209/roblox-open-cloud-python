from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_inventory_api_models_collectible_user_asset_model_builders_club_membership_type import (
    RobloxInventoryApiModelsCollectibleUserAssetModelBuildersClubMembershipType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxInventoryApiModelsCollectibleUserAssetModel")


@_attrs_define
class RobloxInventoryApiModelsCollectibleUserAssetModel:
    """A model containing information about a Roblox.Platform.AssetOwnership.UserAsset

    Attributes:
        user_asset_id (int | Unset): The user asset id
        serial_number (int | Unset): The serial number of the user asset
        asset_id (int | Unset): The asset id of the user asset
        name (str | Unset): The asset name of the asset
        recent_average_price (int | Unset): The recent average price of the asset
        original_price (int | Unset): The original price of the asset
        asset_stock (int | Unset): The recent average price of the user asset
        builders_club_membership_type (RobloxInventoryApiModelsCollectibleUserAssetModelBuildersClubMembershipType |
            Unset): The recent average price of the user asset ['None' = 0, 'BC' = 1, 'TBC' = 2, 'OBC' = 3, 'RobloxPremium'
            = 4]
        is_on_hold (bool | Unset): Whether the user asset has an active hold.
    """

    user_asset_id: int | Unset = UNSET
    serial_number: int | Unset = UNSET
    asset_id: int | Unset = UNSET
    name: str | Unset = UNSET
    recent_average_price: int | Unset = UNSET
    original_price: int | Unset = UNSET
    asset_stock: int | Unset = UNSET
    builders_club_membership_type: (
        RobloxInventoryApiModelsCollectibleUserAssetModelBuildersClubMembershipType | Unset
    ) = UNSET
    is_on_hold: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_asset_id = self.user_asset_id

        serial_number = self.serial_number

        asset_id = self.asset_id

        name = self.name

        recent_average_price = self.recent_average_price

        original_price = self.original_price

        asset_stock = self.asset_stock

        builders_club_membership_type: int | Unset = UNSET
        if not isinstance(self.builders_club_membership_type, Unset):
            builders_club_membership_type = self.builders_club_membership_type.value

        is_on_hold = self.is_on_hold

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_asset_id is not UNSET:
            field_dict["userAssetId"] = user_asset_id
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
        if builders_club_membership_type is not UNSET:
            field_dict["buildersClubMembershipType"] = builders_club_membership_type
        if is_on_hold is not UNSET:
            field_dict["isOnHold"] = is_on_hold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_asset_id = d.pop("userAssetId", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        asset_id = d.pop("assetId", UNSET)

        name = d.pop("name", UNSET)

        recent_average_price = d.pop("recentAveragePrice", UNSET)

        original_price = d.pop("originalPrice", UNSET)

        asset_stock = d.pop("assetStock", UNSET)

        _builders_club_membership_type = d.pop("buildersClubMembershipType", UNSET)
        builders_club_membership_type: (
            RobloxInventoryApiModelsCollectibleUserAssetModelBuildersClubMembershipType | Unset
        )
        if isinstance(_builders_club_membership_type, Unset):
            builders_club_membership_type = UNSET
        else:
            builders_club_membership_type = RobloxInventoryApiModelsCollectibleUserAssetModelBuildersClubMembershipType(
                _builders_club_membership_type
            )

        is_on_hold = d.pop("isOnHold", UNSET)

        roblox_inventory_api_models_collectible_user_asset_model = cls(
            user_asset_id=user_asset_id,
            serial_number=serial_number,
            asset_id=asset_id,
            name=name,
            recent_average_price=recent_average_price,
            original_price=original_price,
            asset_stock=asset_stock,
            builders_club_membership_type=builders_club_membership_type,
            is_on_hold=is_on_hold,
        )

        return roblox_inventory_api_models_collectible_user_asset_model
