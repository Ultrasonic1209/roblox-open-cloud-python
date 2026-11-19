from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_rental_option import RobloxItemConfigurationApiRentalOption


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsMarketplaceItemRegionalRentalPrice")


@_attrs_define
class RobloxItemConfigurationApiModelsMarketplaceItemRegionalRentalPrice:
    """The rental prices for a specific region.

    Attributes:
        country_iso_2_code (str | Unset): The ISO2 code of the country.
        rental_prices (list[RobloxItemConfigurationApiRentalOption] | Unset): The rental prices available in the region.
    """

    country_iso_2_code: str | Unset = UNSET
    rental_prices: list[RobloxItemConfigurationApiRentalOption] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country_iso_2_code = self.country_iso_2_code

        rental_prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rental_prices, Unset):
            rental_prices = []
            for rental_prices_item_data in self.rental_prices:
                rental_prices_item = rental_prices_item_data.to_dict()
                rental_prices.append(rental_prices_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country_iso_2_code is not UNSET:
            field_dict["countryIso2Code"] = country_iso_2_code
        if rental_prices is not UNSET:
            field_dict["rentalPrices"] = rental_prices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_rental_option import RobloxItemConfigurationApiRentalOption  # noqa: PLC0415

        d = dict(src_dict)
        country_iso_2_code = d.pop("countryIso2Code", UNSET)

        _rental_prices = d.pop("rentalPrices", UNSET)
        rental_prices: list[RobloxItemConfigurationApiRentalOption] | Unset = UNSET
        if _rental_prices is not UNSET:
            rental_prices = []
            for rental_prices_item_data in _rental_prices:
                rental_prices_item = RobloxItemConfigurationApiRentalOption.from_dict(rental_prices_item_data)

                rental_prices.append(rental_prices_item)

        roblox_item_configuration_api_models_marketplace_item_regional_rental_price = cls(
            country_iso_2_code=country_iso_2_code,
            rental_prices=rental_prices,
        )

        return roblox_item_configuration_api_models_marketplace_item_regional_rental_price
