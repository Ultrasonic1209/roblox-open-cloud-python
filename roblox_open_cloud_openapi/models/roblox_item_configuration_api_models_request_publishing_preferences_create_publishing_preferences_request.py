from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_request_publishing_preferences_create_publishing_preferences_request_publishing_type import (
    RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestPublishingType,
)
from ..models.roblox_item_configuration_api_models_request_publishing_preferences_create_publishing_preferences_request_sale_location_type import (
    RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestSaleLocationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequest:
    """
    Attributes:
        creator_user_id (int | Unset):
        creator_group_id (int | Unset):
        publishing_type
            (RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestPublishingType |
            Unset): Publishing type for the collectible. Currently can be either Limited or NonLimited. ['Invalid' = 0,
            'Limited' = 1, 'NonLimited' = 2]
        sale_location_type
            (RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestSaleLocationType
            | Unset): Represents possible SaleLocation types of the Collectibles System. ['SALE_LOCATION_TYPE_INVALID' = 0,
            'SALE_LOCATION_TYPE_SHOP_AND_ALL_EXPERIENCES' = 1, 'SALE_LOCATION_EXPERIENCES_AND_DEV_API_ONLY' = 2,
            'SALE_LOCATION_TYPE_SHOP_ONLY' = 3, 'SALE_LOCATION_TYPE_SHOP_AND_EXPERIENCES_BY_ID' = 4]
        places (list[int] | Unset):
        price_in_robux (int | Unset):
        price_offset (int | Unset):
        is_free (bool | Unset):
        enable_regional_pricing (bool | Unset):
        is_rental_opt_in (bool | Unset):
        auto_publish_enabled (bool | Unset):
    """

    creator_user_id: int | Unset = UNSET
    creator_group_id: int | Unset = UNSET
    publishing_type: (
        RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestPublishingType
        | Unset
    ) = UNSET
    sale_location_type: (
        RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestSaleLocationType
        | Unset
    ) = UNSET
    places: list[int] | Unset = UNSET
    price_in_robux: int | Unset = UNSET
    price_offset: int | Unset = UNSET
    is_free: bool | Unset = UNSET
    enable_regional_pricing: bool | Unset = UNSET
    is_rental_opt_in: bool | Unset = UNSET
    auto_publish_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creator_user_id = self.creator_user_id

        creator_group_id = self.creator_group_id

        publishing_type: int | Unset = UNSET
        if not isinstance(self.publishing_type, Unset):
            publishing_type = self.publishing_type.value

        sale_location_type: int | Unset = UNSET
        if not isinstance(self.sale_location_type, Unset):
            sale_location_type = self.sale_location_type.value

        places: list[int] | Unset = UNSET
        if not isinstance(self.places, Unset):
            places = self.places

        price_in_robux = self.price_in_robux

        price_offset = self.price_offset

        is_free = self.is_free

        enable_regional_pricing = self.enable_regional_pricing

        is_rental_opt_in = self.is_rental_opt_in

        auto_publish_enabled = self.auto_publish_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creator_user_id is not UNSET:
            field_dict["creatorUserId"] = creator_user_id
        if creator_group_id is not UNSET:
            field_dict["creatorGroupId"] = creator_group_id
        if publishing_type is not UNSET:
            field_dict["publishingType"] = publishing_type
        if sale_location_type is not UNSET:
            field_dict["saleLocationType"] = sale_location_type
        if places is not UNSET:
            field_dict["places"] = places
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux
        if price_offset is not UNSET:
            field_dict["priceOffset"] = price_offset
        if is_free is not UNSET:
            field_dict["isFree"] = is_free
        if enable_regional_pricing is not UNSET:
            field_dict["enableRegionalPricing"] = enable_regional_pricing
        if is_rental_opt_in is not UNSET:
            field_dict["isRentalOptIn"] = is_rental_opt_in
        if auto_publish_enabled is not UNSET:
            field_dict["autoPublishEnabled"] = auto_publish_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        creator_user_id = d.pop("creatorUserId", UNSET)

        creator_group_id = d.pop("creatorGroupId", UNSET)

        _publishing_type = d.pop("publishingType", UNSET)
        publishing_type: (
            RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestPublishingType
            | Unset
        )
        if isinstance(_publishing_type, Unset):
            publishing_type = UNSET
        else:
            publishing_type = RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestPublishingType(
                _publishing_type
            )

        _sale_location_type = d.pop("saleLocationType", UNSET)
        sale_location_type: (
            RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestSaleLocationType
            | Unset
        )
        if isinstance(_sale_location_type, Unset):
            sale_location_type = UNSET
        else:
            sale_location_type = RobloxItemConfigurationApiModelsRequestPublishingPreferencesCreatePublishingPreferencesRequestSaleLocationType(
                _sale_location_type
            )

        places = cast(list[int], d.pop("places", UNSET))

        price_in_robux = d.pop("priceInRobux", UNSET)

        price_offset = d.pop("priceOffset", UNSET)

        is_free = d.pop("isFree", UNSET)

        enable_regional_pricing = d.pop("enableRegionalPricing", UNSET)

        is_rental_opt_in = d.pop("isRentalOptIn", UNSET)

        auto_publish_enabled = d.pop("autoPublishEnabled", UNSET)

        roblox_item_configuration_api_models_request_publishing_preferences_create_publishing_preferences_request = cls(
            creator_user_id=creator_user_id,
            creator_group_id=creator_group_id,
            publishing_type=publishing_type,
            sale_location_type=sale_location_type,
            places=places,
            price_in_robux=price_in_robux,
            price_offset=price_offset,
            is_free=is_free,
            enable_regional_pricing=enable_regional_pricing,
            is_rental_opt_in=is_rental_opt_in,
            auto_publish_enabled=auto_publish_enabled,
        )

        return roblox_item_configuration_api_models_request_publishing_preferences_create_publishing_preferences_request
