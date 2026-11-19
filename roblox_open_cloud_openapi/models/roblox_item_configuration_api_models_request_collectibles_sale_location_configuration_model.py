from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_request_collectibles_sale_location_configuration_model_sale_location_type import (
    RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModelSaleLocationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModel:
    """Model for Sale Location of Collectible Items.

    Attributes:
        sale_location_type
            (RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModelSaleLocationType | Unset): Rob
            lox.ItemConfiguration.Api.Models.Request.CollectiblesSaleLocationConfigurationModel.CollectiblesSaleLocationType
            . ['SALE_LOCATION_TYPE_INVALID' = 0, 'SALE_LOCATION_TYPE_SHOP_AND_ALL_EXPERIENCES' = 1,
            'SALE_LOCATION_EXPERIENCES_AND_DEV_API_ONLY' = 2, 'SALE_LOCATION_TYPE_SHOP_ONLY' = 3,
            'SALE_LOCATION_TYPE_SHOP_AND_EXPERIENCES_BY_ID' = 4]
        places (list[int] | Unset): The list of PlaceIds this item is allowed to be sold in.
            This will be translated to UniverseIds inside the Collectibles Gateway.
            Requires Roblox.ItemConfiguration.Api.Models.Request.CollectiblesSaleLocationConfigurationModel.CollectiblesSale
            LocationType set to ExperiencesById.
    """

    sale_location_type: (
        RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModelSaleLocationType | Unset
    ) = UNSET
    places: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sale_location_type: int | Unset = UNSET
        if not isinstance(self.sale_location_type, Unset):
            sale_location_type = self.sale_location_type.value

        places: list[int] | Unset = UNSET
        if not isinstance(self.places, Unset):
            places = self.places

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sale_location_type is not UNSET:
            field_dict["saleLocationType"] = sale_location_type
        if places is not UNSET:
            field_dict["places"] = places

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sale_location_type = d.pop("saleLocationType", UNSET)
        sale_location_type: (
            RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModelSaleLocationType | Unset
        )
        if isinstance(_sale_location_type, Unset):
            sale_location_type = UNSET
        else:
            sale_location_type = (
                RobloxItemConfigurationApiModelsRequestCollectiblesSaleLocationConfigurationModelSaleLocationType(
                    _sale_location_type
                )
            )

        places = cast(list[int], d.pop("places", UNSET))

        roblox_item_configuration_api_models_request_collectibles_sale_location_configuration_model = cls(
            sale_location_type=sale_location_type,
            places=places,
        )

        return roblox_item_configuration_api_models_request_collectibles_sale_location_configuration_model
