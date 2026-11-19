from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_marketplace_item_regional_rental_price import (
        RobloxItemConfigurationApiModelsMarketplaceItemRegionalRentalPrice,
    )
    from ..models.roblox_item_configuration_api_rental_option import RobloxItemConfigurationApiRentalOption


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseGetRentalPricingPreviewResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseGetRentalPricingPreviewResponse:
    """Defines the response model for the POST v1/collectibles/rental-pricing/preview.

    Attributes:
        rental_prices (list[RobloxItemConfigurationApiRentalOption] | Unset): Rental prices for the given target.
        regional_rental_prices (list[RobloxItemConfigurationApiModelsMarketplaceItemRegionalRentalPrice] | Unset): The
            regional rental prices for the given target.
    """

    rental_prices: list[RobloxItemConfigurationApiRentalOption] | Unset = UNSET
    regional_rental_prices: list[RobloxItemConfigurationApiModelsMarketplaceItemRegionalRentalPrice] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        rental_prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rental_prices, Unset):
            rental_prices = []
            for rental_prices_item_data in self.rental_prices:
                rental_prices_item = rental_prices_item_data.to_dict()
                rental_prices.append(rental_prices_item)

        regional_rental_prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regional_rental_prices, Unset):
            regional_rental_prices = []
            for regional_rental_prices_item_data in self.regional_rental_prices:
                regional_rental_prices_item = regional_rental_prices_item_data.to_dict()
                regional_rental_prices.append(regional_rental_prices_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rental_prices is not UNSET:
            field_dict["rentalPrices"] = rental_prices
        if regional_rental_prices is not UNSET:
            field_dict["regionalRentalPrices"] = regional_rental_prices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_marketplace_item_regional_rental_price import (
            RobloxItemConfigurationApiModelsMarketplaceItemRegionalRentalPrice,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_rental_option import RobloxItemConfigurationApiRentalOption  # noqa: PLC0415

        d = dict(src_dict)
        _rental_prices = d.pop("rentalPrices", UNSET)
        rental_prices: list[RobloxItemConfigurationApiRentalOption] | Unset = UNSET
        if _rental_prices is not UNSET:
            rental_prices = []
            for rental_prices_item_data in _rental_prices:
                rental_prices_item = RobloxItemConfigurationApiRentalOption.from_dict(rental_prices_item_data)

                rental_prices.append(rental_prices_item)

        _regional_rental_prices = d.pop("regionalRentalPrices", UNSET)
        regional_rental_prices: list[RobloxItemConfigurationApiModelsMarketplaceItemRegionalRentalPrice] | Unset = UNSET
        if _regional_rental_prices is not UNSET:
            regional_rental_prices = []
            for regional_rental_prices_item_data in _regional_rental_prices:
                regional_rental_prices_item = (
                    RobloxItemConfigurationApiModelsMarketplaceItemRegionalRentalPrice.from_dict(
                        regional_rental_prices_item_data
                    )
                )

                regional_rental_prices.append(regional_rental_prices_item)

        roblox_item_configuration_api_models_response_get_rental_pricing_preview_response = cls(
            rental_prices=rental_prices,
            regional_rental_prices=regional_rental_prices,
        )

        return roblox_item_configuration_api_models_response_get_rental_pricing_preview_response
