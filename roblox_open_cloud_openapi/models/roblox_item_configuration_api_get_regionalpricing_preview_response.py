from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_regional_price import RobloxItemConfigurationApiRegionalPrice


T = TypeVar("T", bound="RobloxItemConfigurationApiGetRegionalpricingPreviewResponse")


@_attrs_define
class RobloxItemConfigurationApiGetRegionalpricingPreviewResponse:
    """Defines the response model for the POST v1/collectibles/regional-pricing/preview.

    Attributes:
        regional_prices (list[RobloxItemConfigurationApiRegionalPrice] | Unset): List of representative countries.
    """

    regional_prices: list[RobloxItemConfigurationApiRegionalPrice] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        regional_prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regional_prices, Unset):
            regional_prices = []
            for regional_prices_item_data in self.regional_prices:
                regional_prices_item = regional_prices_item_data.to_dict()
                regional_prices.append(regional_prices_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if regional_prices is not UNSET:
            field_dict["regionalPrices"] = regional_prices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_regional_price import RobloxItemConfigurationApiRegionalPrice  # noqa: PLC0415

        d = dict(src_dict)
        _regional_prices = d.pop("regionalPrices", UNSET)
        regional_prices: list[RobloxItemConfigurationApiRegionalPrice] | Unset = UNSET
        if _regional_prices is not UNSET:
            regional_prices = []
            for regional_prices_item_data in _regional_prices:
                regional_prices_item = RobloxItemConfigurationApiRegionalPrice.from_dict(regional_prices_item_data)

                regional_prices.append(regional_prices_item)

        roblox_item_configuration_api_get_regionalpricing_preview_response = cls(
            regional_prices=regional_prices,
        )

        return roblox_item_configuration_api_get_regionalpricing_preview_response
