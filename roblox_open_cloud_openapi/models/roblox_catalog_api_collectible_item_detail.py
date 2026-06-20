from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_collectible_item_detail_collectible_item_type import (
    RobloxCatalogApiCollectibleItemDetailCollectibleItemType,
)
from ..models.roblox_catalog_api_collectible_item_detail_resale_restriction import (
    RobloxCatalogApiCollectibleItemDetailResaleRestriction,
)
from ..models.roblox_catalog_api_collectible_item_detail_sale_status import (
    RobloxCatalogApiCollectibleItemDetailSaleStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_sale_location import RobloxCatalogApiSaleLocation


T = TypeVar("T", bound="RobloxCatalogApiCollectibleItemDetail")


@_attrs_define
class RobloxCatalogApiCollectibleItemDetail:
    """
    Attributes:
        collectible_item_id (str | Unset):
        collectible_product_id (str | Unset):
        price (int | Unset):
        lowest_price (int | Unset):
        lowest_resale_price (int | Unset):
        total_quantity (int | Unset):
        units_available (int | Unset):
        sale_location (RobloxCatalogApiSaleLocation | Unset): SaleLocation information for a collectible item (asset or
            bundle).
        has_resellers (bool | Unset):
        sale_status (RobloxCatalogApiCollectibleItemDetailSaleStatus | Unset):  ['Invalid' = 0, 'Draft' = 1, 'OffSale' =
            2, 'OnSale' = 3, 'PendingSale' = 4]
        quantity_limit_per_user (int | Unset):
        off_sale_deadline (datetime.datetime | Unset):
        collectible_item_type (RobloxCatalogApiCollectibleItemDetailCollectibleItemType | Unset): The type of
            collectible item, limited or non-limited for now. ['Invalid' = 0, 'Limited' = 1, 'NonLimited' = 2]
        lowest_available_resale_product_id (str | Unset):
        lowest_available_resale_item_instance_id (str | Unset):
        resale_restriction (RobloxCatalogApiCollectibleItemDetailResaleRestriction | Unset):  ['Invalid' = 0, 'None' =
            1, 'Disabled' = 2]
    """

    collectible_item_id: str | Unset = UNSET
    collectible_product_id: str | Unset = UNSET
    price: int | Unset = UNSET
    lowest_price: int | Unset = UNSET
    lowest_resale_price: int | Unset = UNSET
    total_quantity: int | Unset = UNSET
    units_available: int | Unset = UNSET
    sale_location: RobloxCatalogApiSaleLocation | Unset = UNSET
    has_resellers: bool | Unset = UNSET
    sale_status: RobloxCatalogApiCollectibleItemDetailSaleStatus | Unset = UNSET
    quantity_limit_per_user: int | Unset = UNSET
    off_sale_deadline: datetime.datetime | Unset = UNSET
    collectible_item_type: RobloxCatalogApiCollectibleItemDetailCollectibleItemType | Unset = UNSET
    lowest_available_resale_product_id: str | Unset = UNSET
    lowest_available_resale_item_instance_id: str | Unset = UNSET
    resale_restriction: RobloxCatalogApiCollectibleItemDetailResaleRestriction | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        collectible_item_id = self.collectible_item_id

        collectible_product_id = self.collectible_product_id

        price = self.price

        lowest_price = self.lowest_price

        lowest_resale_price = self.lowest_resale_price

        total_quantity = self.total_quantity

        units_available = self.units_available

        sale_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sale_location, Unset):
            sale_location = self.sale_location.to_dict()

        has_resellers = self.has_resellers

        sale_status: int | Unset = UNSET
        if not isinstance(self.sale_status, Unset):
            sale_status = self.sale_status.value

        quantity_limit_per_user = self.quantity_limit_per_user

        off_sale_deadline: str | Unset = UNSET
        if not isinstance(self.off_sale_deadline, Unset):
            off_sale_deadline = self.off_sale_deadline.isoformat()

        collectible_item_type: int | Unset = UNSET
        if not isinstance(self.collectible_item_type, Unset):
            collectible_item_type = self.collectible_item_type.value

        lowest_available_resale_product_id = self.lowest_available_resale_product_id

        lowest_available_resale_item_instance_id = self.lowest_available_resale_item_instance_id

        resale_restriction: int | Unset = UNSET
        if not isinstance(self.resale_restriction, Unset):
            resale_restriction = self.resale_restriction.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if collectible_item_id is not UNSET:
            field_dict["collectibleItemId"] = collectible_item_id
        if collectible_product_id is not UNSET:
            field_dict["collectibleProductId"] = collectible_product_id
        if price is not UNSET:
            field_dict["price"] = price
        if lowest_price is not UNSET:
            field_dict["lowestPrice"] = lowest_price
        if lowest_resale_price is not UNSET:
            field_dict["lowestResalePrice"] = lowest_resale_price
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity
        if units_available is not UNSET:
            field_dict["unitsAvailable"] = units_available
        if sale_location is not UNSET:
            field_dict["saleLocation"] = sale_location
        if has_resellers is not UNSET:
            field_dict["hasResellers"] = has_resellers
        if sale_status is not UNSET:
            field_dict["saleStatus"] = sale_status
        if quantity_limit_per_user is not UNSET:
            field_dict["quantityLimitPerUser"] = quantity_limit_per_user
        if off_sale_deadline is not UNSET:
            field_dict["offSaleDeadline"] = off_sale_deadline
        if collectible_item_type is not UNSET:
            field_dict["collectibleItemType"] = collectible_item_type
        if lowest_available_resale_product_id is not UNSET:
            field_dict["lowestAvailableResaleProductId"] = lowest_available_resale_product_id
        if lowest_available_resale_item_instance_id is not UNSET:
            field_dict["lowestAvailableResaleItemInstanceId"] = lowest_available_resale_item_instance_id
        if resale_restriction is not UNSET:
            field_dict["resaleRestriction"] = resale_restriction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_sale_location import RobloxCatalogApiSaleLocation

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        collectible_item_id = d.pop("collectibleItemId", UNSET)

        collectible_product_id = d.pop("collectibleProductId", UNSET)

        price = d.pop("price", UNSET)

        lowest_price = d.pop("lowestPrice", UNSET)

        lowest_resale_price = d.pop("lowestResalePrice", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        units_available = d.pop("unitsAvailable", UNSET)

        _sale_location = d.pop("saleLocation", UNSET)
        sale_location: RobloxCatalogApiSaleLocation | Unset
        if isinstance(_sale_location, Unset):
            sale_location = UNSET
        else:
            sale_location = RobloxCatalogApiSaleLocation.from_dict(_sale_location)

        has_resellers = d.pop("hasResellers", UNSET)

        _sale_status = d.pop("saleStatus", UNSET)
        sale_status: RobloxCatalogApiCollectibleItemDetailSaleStatus | Unset
        if isinstance(_sale_status, Unset):
            sale_status = UNSET
        else:
            sale_status = RobloxCatalogApiCollectibleItemDetailSaleStatus(_sale_status)

        quantity_limit_per_user = d.pop("quantityLimitPerUser", UNSET)

        _off_sale_deadline = d.pop("offSaleDeadline", UNSET)
        off_sale_deadline: datetime.datetime | Unset
        if isinstance(_off_sale_deadline, Unset):
            off_sale_deadline = UNSET
        else:
            off_sale_deadline = datetime.datetime.fromisoformat(_off_sale_deadline)

        _collectible_item_type = d.pop("collectibleItemType", UNSET)
        collectible_item_type: RobloxCatalogApiCollectibleItemDetailCollectibleItemType | Unset
        if isinstance(_collectible_item_type, Unset):
            collectible_item_type = UNSET
        else:
            collectible_item_type = RobloxCatalogApiCollectibleItemDetailCollectibleItemType(_collectible_item_type)

        lowest_available_resale_product_id = d.pop("lowestAvailableResaleProductId", UNSET)

        lowest_available_resale_item_instance_id = d.pop("lowestAvailableResaleItemInstanceId", UNSET)

        _resale_restriction = d.pop("resaleRestriction", UNSET)
        resale_restriction: RobloxCatalogApiCollectibleItemDetailResaleRestriction | Unset
        if isinstance(_resale_restriction, Unset):
            resale_restriction = UNSET
        else:
            resale_restriction = RobloxCatalogApiCollectibleItemDetailResaleRestriction(_resale_restriction)

        roblox_catalog_api_collectible_item_detail = cls(
            collectible_item_id=collectible_item_id,
            collectible_product_id=collectible_product_id,
            price=price,
            lowest_price=lowest_price,
            lowest_resale_price=lowest_resale_price,
            total_quantity=total_quantity,
            units_available=units_available,
            sale_location=sale_location,
            has_resellers=has_resellers,
            sale_status=sale_status,
            quantity_limit_per_user=quantity_limit_per_user,
            off_sale_deadline=off_sale_deadline,
            collectible_item_type=collectible_item_type,
            lowest_available_resale_product_id=lowest_available_resale_product_id,
            lowest_available_resale_item_instance_id=lowest_available_resale_item_instance_id,
            resale_restriction=resale_restriction,
        )

        return roblox_catalog_api_collectible_item_detail
