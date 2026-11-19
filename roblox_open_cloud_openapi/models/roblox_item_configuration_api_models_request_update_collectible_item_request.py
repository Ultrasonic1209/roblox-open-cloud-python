from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_request_update_collectible_item_request_resale_restriction import (
    RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestResaleRestriction,
)
from ..models.roblox_item_configuration_api_models_request_update_collectible_item_request_sale_status import (
    RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestSaleStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_request_collectibles_sale_location_configuration_model import (
        RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequest:
    """Api request to update a collectible item.

    Attributes:
        sale_location_configuration (RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel |
            Unset): Model for Sale Location of Collectible Items.
        is_rental_opt_in (bool | Unset): Whether the item is opted into rental.
        sale_status (RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestSaleStatus | Unset): The new
            sale status for the associated CollectibleItem.
            OnSale and OffSale are the only valid values. ['OnSale' = 0, 'OffSale' = 1, 'Free' = 2]
        quantity_limit_per_user (int | Unset): The max number of instances for the CollectibleItem a user can own.
        resale_restriction (RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestResaleRestriction |
            Unset): The resale restriction of the CollectibleItem. ['INVALID' = 0, 'NONE' = 1, 'DISABLED' = 2]
        price_in_robux (int | Unset): The minimum price of the CollectibleItem.
        price_offset (int | Unset): The price offset of the item in Robux above the price floor.
        opt_out_from_regional_pricing (bool | Unset): Whether to opt out of the regional pricing.
        is_free (bool | Unset): Whether or not the item is free.
            If it's free, the MinimumPrice and PriceOffset values are ignored.
        on_sale_time (datetime.datetime | Unset): Scheduled on sale time for publishing the item.
        off_sale_time (datetime.datetime | Unset): Scheduled off sale time for publishing the item.
    """

    sale_location_configuration: (
        RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel | Unset
    ) = UNSET
    is_rental_opt_in: bool | Unset = UNSET
    sale_status: RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestSaleStatus | Unset = UNSET
    quantity_limit_per_user: int | Unset = UNSET
    resale_restriction: RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestResaleRestriction | Unset = (
        UNSET
    )
    price_in_robux: int | Unset = UNSET
    price_offset: int | Unset = UNSET
    opt_out_from_regional_pricing: bool | Unset = UNSET
    is_free: bool | Unset = UNSET
    on_sale_time: datetime.datetime | Unset = UNSET
    off_sale_time: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sale_location_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sale_location_configuration, Unset):
            sale_location_configuration = self.sale_location_configuration.to_dict()

        is_rental_opt_in = self.is_rental_opt_in

        sale_status: int | Unset = UNSET
        if not isinstance(self.sale_status, Unset):
            sale_status = self.sale_status.value

        quantity_limit_per_user = self.quantity_limit_per_user

        resale_restriction: int | Unset = UNSET
        if not isinstance(self.resale_restriction, Unset):
            resale_restriction = self.resale_restriction.value

        price_in_robux = self.price_in_robux

        price_offset = self.price_offset

        opt_out_from_regional_pricing = self.opt_out_from_regional_pricing

        is_free = self.is_free

        on_sale_time: str | Unset = UNSET
        if not isinstance(self.on_sale_time, Unset):
            on_sale_time = self.on_sale_time.isoformat()

        off_sale_time: str | Unset = UNSET
        if not isinstance(self.off_sale_time, Unset):
            off_sale_time = self.off_sale_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sale_location_configuration is not UNSET:
            field_dict["saleLocationConfiguration"] = sale_location_configuration
        if is_rental_opt_in is not UNSET:
            field_dict["isRentalOptIn"] = is_rental_opt_in
        if sale_status is not UNSET:
            field_dict["saleStatus"] = sale_status
        if quantity_limit_per_user is not UNSET:
            field_dict["quantityLimitPerUser"] = quantity_limit_per_user
        if resale_restriction is not UNSET:
            field_dict["resaleRestriction"] = resale_restriction
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux
        if price_offset is not UNSET:
            field_dict["priceOffset"] = price_offset
        if opt_out_from_regional_pricing is not UNSET:
            field_dict["optOutFromRegionalPricing"] = opt_out_from_regional_pricing
        if is_free is not UNSET:
            field_dict["isFree"] = is_free
        if on_sale_time is not UNSET:
            field_dict["onSaleTime"] = on_sale_time
        if off_sale_time is not UNSET:
            field_dict["offSaleTime"] = off_sale_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_request_collectibles_sale_location_configuration_model import (
            RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _sale_location_configuration = d.pop("saleLocationConfiguration", UNSET)
        sale_location_configuration: (
            RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel | Unset
        )
        if isinstance(_sale_location_configuration, Unset):
            sale_location_configuration = UNSET
        else:
            sale_location_configuration = (
                RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel.from_dict(
                    _sale_location_configuration
                )
            )

        is_rental_opt_in = d.pop("isRentalOptIn", UNSET)

        _sale_status = d.pop("saleStatus", UNSET)
        sale_status: RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestSaleStatus | Unset
        if isinstance(_sale_status, Unset):
            sale_status = UNSET
        else:
            sale_status = RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestSaleStatus(_sale_status)

        quantity_limit_per_user = d.pop("quantityLimitPerUser", UNSET)

        _resale_restriction = d.pop("resaleRestriction", UNSET)
        resale_restriction: RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestResaleRestriction | Unset
        if isinstance(_resale_restriction, Unset):
            resale_restriction = UNSET
        else:
            resale_restriction = RobloxItemConfigurationApiModelsRequestUpdateCollectibleItemRequestResaleRestriction(
                _resale_restriction
            )

        price_in_robux = d.pop("priceInRobux", UNSET)

        price_offset = d.pop("priceOffset", UNSET)

        opt_out_from_regional_pricing = d.pop("optOutFromRegionalPricing", UNSET)

        is_free = d.pop("isFree", UNSET)

        _on_sale_time = d.pop("onSaleTime", UNSET)
        on_sale_time: datetime.datetime | Unset
        if isinstance(_on_sale_time, Unset):
            on_sale_time = UNSET
        else:
            on_sale_time = datetime.datetime.fromisoformat(_on_sale_time)

        _off_sale_time = d.pop("offSaleTime", UNSET)
        off_sale_time: datetime.datetime | Unset
        if isinstance(_off_sale_time, Unset):
            off_sale_time = UNSET
        else:
            off_sale_time = datetime.datetime.fromisoformat(_off_sale_time)

        roblox_item_configuration_api_models_request_update_collectible_item_request = cls(
            sale_location_configuration=sale_location_configuration,
            is_rental_opt_in=is_rental_opt_in,
            sale_status=sale_status,
            quantity_limit_per_user=quantity_limit_per_user,
            resale_restriction=resale_restriction,
            price_in_robux=price_in_robux,
            price_offset=price_offset,
            opt_out_from_regional_pricing=opt_out_from_regional_pricing,
            is_free=is_free,
            on_sale_time=on_sale_time,
            off_sale_time=off_sale_time,
        )

        return roblox_item_configuration_api_models_request_update_collectible_item_request
