from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_marketplace_item_sale_location_sale_location_type import (
    RobloxItemConfigurationApiModelsMarketplaceItemSaleLocationSaleLocationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsMarketplaceItemSaleLocation")


@_attrs_define
class RobloxItemConfigurationApiModelsMarketplaceItemSaleLocation:
    """The collectible sale location.

    Attributes:
        sale_location_type (RobloxItemConfigurationApiModelsMarketplaceItemSaleLocationSaleLocationType | Unset): The
            sale location type. ['SALE_LOCATION_TYPE_INVALID' = 0, 'SALE_LOCATION_TYPE_SHOP_AND_ALL_EXPERIENCES' = 1,
            'SALE_LOCATION_EXPERIENCES_AND_DEV_API_ONLY' = 2, 'SALE_LOCATION_TYPE_SHOP_ONLY' = 3,
            'SALE_LOCATION_TYPE_SHOP_AND_EXPERIENCES_BY_ID' = 4]
        universe_ids (list[int] | Unset): The universe ids the collectible item may be sold in.
    """

    sale_location_type: RobloxItemConfigurationApiModelsMarketplaceItemSaleLocationSaleLocationType | Unset = UNSET
    universe_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sale_location_type: int | Unset = UNSET
        if not isinstance(self.sale_location_type, Unset):
            sale_location_type = self.sale_location_type.value

        universe_ids: list[int] | Unset = UNSET
        if not isinstance(self.universe_ids, Unset):
            universe_ids = self.universe_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sale_location_type is not UNSET:
            field_dict["saleLocationType"] = sale_location_type
        if universe_ids is not UNSET:
            field_dict["universeIds"] = universe_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sale_location_type = d.pop("saleLocationType", UNSET)
        sale_location_type: RobloxItemConfigurationApiModelsMarketplaceItemSaleLocationSaleLocationType | Unset
        if isinstance(_sale_location_type, Unset):
            sale_location_type = UNSET
        else:
            sale_location_type = RobloxItemConfigurationApiModelsMarketplaceItemSaleLocationSaleLocationType(
                _sale_location_type
            )

        universe_ids = cast(list[int], d.pop("universeIds", UNSET))

        roblox_item_configuration_api_models_marketplace_item_sale_location = cls(
            sale_location_type=sale_location_type,
            universe_ids=universe_ids,
        )

        return roblox_item_configuration_api_models_marketplace_item_sale_location
