from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_collectibles_metadata_response_allowed_collectible_sale_locations_item import (
    RobloxItemConfigurationApiCollectiblesMetadataResponseAllowedCollectibleSaleLocationsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_revenue_split_tier import RobloxItemConfigurationApiRevenueSplitTier
    from ..models.roblox_item_configuration_api_scheduled_publishing_settings import (
        RobloxItemConfigurationApiScheduledPublishingSettings,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiCollectiblesMetadataResponse")


@_attrs_define
class RobloxItemConfigurationApiCollectiblesMetadataResponse:
    """
    Attributes:
        is_collectibles_controller_enabled (bool | Unset): Determines if the Collectibles controller and its APIs are
            enabled.
        is_collectibles_publishing_enabled (bool | Unset): Determines if publishing Collectible Items is enabled.
        is_collectibles_publishing_location_type_enabled (bool | Unset): Determines if other sale locations are enabled.
        allowed_collectible_sale_locations
            (list[RobloxItemConfigurationApiCollectiblesMetadataResponseAllowedCollectibleSaleLocationsItem] | Unset): The
            list of available SaleLocations for collectible items.
        is_collectible_free_item_publishing_available (bool | Unset): Whether or not publishing free Collectibles is
            allowed.
        is_collectible_group_publishing_available (bool | Unset): Whether or not publishing Collectibles for groups is
            allowed.
        is_collectible_resale_restrictions_enabled (bool | Unset): Whether or not resale restrictions for Collectibles
            are enabled.
        is_collectible_publish_min_quantity_enabled (bool | Unset): Whether or not minimum quantity for Collectibles are
            enabled.
        is_ugc_4_all_ui_enabled (bool | Unset): Flag whether the new UI is enabled.
        limited_max_quantity (int | Unset): The maximum quantity for limited item publishing.
        max_collectible_price (int | Unset): The maximum price for a collectible item.
        is_limited_collectible_bundles_publishing_enabled (bool | Unset): Determines whether limited collectible bundles
            publishing is enabled.
        is_resellability_enabled (bool | Unset): Whether or not publishing resellable items is enabled.
        is_new_bundle_ui_enabled (bool | Unset): Whether or not dpf bundle UI is enabled.
        is_collectible_2d_publishing_enabled (bool | Unset): Whether or not collectible 2D publishing is enabled.
        is_avatar_creation_tokens_ui_enabled (bool | Unset): Whether or not the avatar creation tokens page
            should be displayed.
        is_scheduled_publishing_enabled (bool | Unset): Whether or not scheduled publishing is enabled.
        scheduled_publishing_settings (RobloxItemConfigurationApiScheduledPublishingSettings | Unset):
        is_get_price_floor_enabled (bool | Unset): Determines whether GetPriceFloorAsync endpoint is enabled.
        is_regional_pricing_enabled (bool | Unset): Whether regional pricing is enabled.
        is_revenue_split_enabled (bool | Unset): Whether revenue split endpoint is enabled.
        revenue_split_tiers_for_purchase (list[RobloxItemConfigurationApiRevenueSplitTier] | Unset): List of revenue
            split tiers for purchase.
        is_content_metadata_appeal_enabled (bool | Unset): Whether content metadata appeals are enabled. Always false;
            the appeal endpoints have been removed.
        bodysuit_eligible_asset_types (list[int] | Unset): List of asset types that are bodysuit eligible.
        unify_configure_ui (bool | Unset): Whether the new configure UI is enabled for 2D assets.
        is_restocking_enabled (bool | Unset): Whether restocking of limited collectible items is enabled.
        restock_resale_lock_duration_seconds (int | Unset): Duration in seconds that resale remains locked after a
            restock. The FE computes the
            unlock time as lastRestockedTime + this duration.
        is_avatar_item_licensing_enabled (bool | Unset): Whether the Avatar Item Licensing feature (UCP-1792) is
            enabled. The frontend shows/hides the
            licensing UI (e.g. the agreement picker) off this value, which mirrors the same server-side
            gate used to enable the licensing behavior.
        is_marketplace_affiliate_link_ui_enabled (bool | Unset): Whether the marketplace affiliate link UI is enabled
            for the authenticated user.
    """

    is_collectibles_controller_enabled: bool | Unset = UNSET
    is_collectibles_publishing_enabled: bool | Unset = UNSET
    is_collectibles_publishing_location_type_enabled: bool | Unset = UNSET
    allowed_collectible_sale_locations: (
        list[RobloxItemConfigurationApiCollectiblesMetadataResponseAllowedCollectibleSaleLocationsItem] | Unset
    ) = UNSET
    is_collectible_free_item_publishing_available: bool | Unset = UNSET
    is_collectible_group_publishing_available: bool | Unset = UNSET
    is_collectible_resale_restrictions_enabled: bool | Unset = UNSET
    is_collectible_publish_min_quantity_enabled: bool | Unset = UNSET
    is_ugc_4_all_ui_enabled: bool | Unset = UNSET
    limited_max_quantity: int | Unset = UNSET
    max_collectible_price: int | Unset = UNSET
    is_limited_collectible_bundles_publishing_enabled: bool | Unset = UNSET
    is_resellability_enabled: bool | Unset = UNSET
    is_new_bundle_ui_enabled: bool | Unset = UNSET
    is_collectible_2d_publishing_enabled: bool | Unset = UNSET
    is_avatar_creation_tokens_ui_enabled: bool | Unset = UNSET
    is_scheduled_publishing_enabled: bool | Unset = UNSET
    scheduled_publishing_settings: RobloxItemConfigurationApiScheduledPublishingSettings | Unset = UNSET
    is_get_price_floor_enabled: bool | Unset = UNSET
    is_regional_pricing_enabled: bool | Unset = UNSET
    is_revenue_split_enabled: bool | Unset = UNSET
    revenue_split_tiers_for_purchase: list[RobloxItemConfigurationApiRevenueSplitTier] | Unset = UNSET
    is_content_metadata_appeal_enabled: bool | Unset = UNSET
    bodysuit_eligible_asset_types: list[int] | Unset = UNSET
    unify_configure_ui: bool | Unset = UNSET
    is_restocking_enabled: bool | Unset = UNSET
    restock_resale_lock_duration_seconds: int | Unset = UNSET
    is_avatar_item_licensing_enabled: bool | Unset = UNSET
    is_marketplace_affiliate_link_ui_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_collectibles_controller_enabled = self.is_collectibles_controller_enabled

        is_collectibles_publishing_enabled = self.is_collectibles_publishing_enabled

        is_collectibles_publishing_location_type_enabled = self.is_collectibles_publishing_location_type_enabled

        allowed_collectible_sale_locations: list[int] | Unset = UNSET
        if not isinstance(self.allowed_collectible_sale_locations, Unset):
            allowed_collectible_sale_locations = []
            for allowed_collectible_sale_locations_item_data in self.allowed_collectible_sale_locations:
                allowed_collectible_sale_locations_item = allowed_collectible_sale_locations_item_data.value
                allowed_collectible_sale_locations.append(allowed_collectible_sale_locations_item)

        is_collectible_free_item_publishing_available = self.is_collectible_free_item_publishing_available

        is_collectible_group_publishing_available = self.is_collectible_group_publishing_available

        is_collectible_resale_restrictions_enabled = self.is_collectible_resale_restrictions_enabled

        is_collectible_publish_min_quantity_enabled = self.is_collectible_publish_min_quantity_enabled

        is_ugc_4_all_ui_enabled = self.is_ugc_4_all_ui_enabled

        limited_max_quantity = self.limited_max_quantity

        max_collectible_price = self.max_collectible_price

        is_limited_collectible_bundles_publishing_enabled = self.is_limited_collectible_bundles_publishing_enabled

        is_resellability_enabled = self.is_resellability_enabled

        is_new_bundle_ui_enabled = self.is_new_bundle_ui_enabled

        is_collectible_2d_publishing_enabled = self.is_collectible_2d_publishing_enabled

        is_avatar_creation_tokens_ui_enabled = self.is_avatar_creation_tokens_ui_enabled

        is_scheduled_publishing_enabled = self.is_scheduled_publishing_enabled

        scheduled_publishing_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scheduled_publishing_settings, Unset):
            scheduled_publishing_settings = self.scheduled_publishing_settings.to_dict()

        is_get_price_floor_enabled = self.is_get_price_floor_enabled

        is_regional_pricing_enabled = self.is_regional_pricing_enabled

        is_revenue_split_enabled = self.is_revenue_split_enabled

        revenue_split_tiers_for_purchase: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.revenue_split_tiers_for_purchase, Unset):
            revenue_split_tiers_for_purchase = []
            for revenue_split_tiers_for_purchase_item_data in self.revenue_split_tiers_for_purchase:
                revenue_split_tiers_for_purchase_item = revenue_split_tiers_for_purchase_item_data.to_dict()
                revenue_split_tiers_for_purchase.append(revenue_split_tiers_for_purchase_item)

        is_content_metadata_appeal_enabled = self.is_content_metadata_appeal_enabled

        bodysuit_eligible_asset_types: list[int] | Unset = UNSET
        if not isinstance(self.bodysuit_eligible_asset_types, Unset):
            bodysuit_eligible_asset_types = self.bodysuit_eligible_asset_types

        unify_configure_ui = self.unify_configure_ui

        is_restocking_enabled = self.is_restocking_enabled

        restock_resale_lock_duration_seconds = self.restock_resale_lock_duration_seconds

        is_avatar_item_licensing_enabled = self.is_avatar_item_licensing_enabled

        is_marketplace_affiliate_link_ui_enabled = self.is_marketplace_affiliate_link_ui_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_collectibles_controller_enabled is not UNSET:
            field_dict["isCollectiblesControllerEnabled"] = is_collectibles_controller_enabled
        if is_collectibles_publishing_enabled is not UNSET:
            field_dict["isCollectiblesPublishingEnabled"] = is_collectibles_publishing_enabled
        if is_collectibles_publishing_location_type_enabled is not UNSET:
            field_dict["isCollectiblesPublishingLocationTypeEnabled"] = is_collectibles_publishing_location_type_enabled
        if allowed_collectible_sale_locations is not UNSET:
            field_dict["allowedCollectibleSaleLocations"] = allowed_collectible_sale_locations
        if is_collectible_free_item_publishing_available is not UNSET:
            field_dict["IsCollectibleFreeItemPublishingAvailable"] = is_collectible_free_item_publishing_available
        if is_collectible_group_publishing_available is not UNSET:
            field_dict["isCollectibleGroupPublishingAvailable"] = is_collectible_group_publishing_available
        if is_collectible_resale_restrictions_enabled is not UNSET:
            field_dict["isCollectibleResaleRestrictionsEnabled"] = is_collectible_resale_restrictions_enabled
        if is_collectible_publish_min_quantity_enabled is not UNSET:
            field_dict["isCollectiblePublishMinQuantityEnabled"] = is_collectible_publish_min_quantity_enabled
        if is_ugc_4_all_ui_enabled is not UNSET:
            field_dict["IsUgc4AllUIEnabled"] = is_ugc_4_all_ui_enabled
        if limited_max_quantity is not UNSET:
            field_dict["LimitedMaxQuantity"] = limited_max_quantity
        if max_collectible_price is not UNSET:
            field_dict["MaxCollectiblePrice"] = max_collectible_price
        if is_limited_collectible_bundles_publishing_enabled is not UNSET:
            field_dict["IsLimitedCollectibleBundlesPublishingEnabled"] = (
                is_limited_collectible_bundles_publishing_enabled
            )
        if is_resellability_enabled is not UNSET:
            field_dict["IsResellabilityEnabled"] = is_resellability_enabled
        if is_new_bundle_ui_enabled is not UNSET:
            field_dict["IsNewBundleUIEnabled"] = is_new_bundle_ui_enabled
        if is_collectible_2d_publishing_enabled is not UNSET:
            field_dict["IsCollectible2DPublishingEnabled"] = is_collectible_2d_publishing_enabled
        if is_avatar_creation_tokens_ui_enabled is not UNSET:
            field_dict["IsAvatarCreationTokensUIEnabled"] = is_avatar_creation_tokens_ui_enabled
        if is_scheduled_publishing_enabled is not UNSET:
            field_dict["IsScheduledPublishingEnabled"] = is_scheduled_publishing_enabled
        if scheduled_publishing_settings is not UNSET:
            field_dict["ScheduledPublishingSettings"] = scheduled_publishing_settings
        if is_get_price_floor_enabled is not UNSET:
            field_dict["isGetPriceFloorEnabled"] = is_get_price_floor_enabled
        if is_regional_pricing_enabled is not UNSET:
            field_dict["isRegionalPricingEnabled"] = is_regional_pricing_enabled
        if is_revenue_split_enabled is not UNSET:
            field_dict["isRevenueSplitEnabled"] = is_revenue_split_enabled
        if revenue_split_tiers_for_purchase is not UNSET:
            field_dict["revenueSplitTiersForPurchase"] = revenue_split_tiers_for_purchase
        if is_content_metadata_appeal_enabled is not UNSET:
            field_dict["isContentMetadataAppealEnabled"] = is_content_metadata_appeal_enabled
        if bodysuit_eligible_asset_types is not UNSET:
            field_dict["bodysuitEligibleAssetTypes"] = bodysuit_eligible_asset_types
        if unify_configure_ui is not UNSET:
            field_dict["unifyConfigureUI"] = unify_configure_ui
        if is_restocking_enabled is not UNSET:
            field_dict["isRestockingEnabled"] = is_restocking_enabled
        if restock_resale_lock_duration_seconds is not UNSET:
            field_dict["restockResaleLockDurationSeconds"] = restock_resale_lock_duration_seconds
        if is_avatar_item_licensing_enabled is not UNSET:
            field_dict["isAvatarItemLicensingEnabled"] = is_avatar_item_licensing_enabled
        if is_marketplace_affiliate_link_ui_enabled is not UNSET:
            field_dict["isMarketplaceAffiliateLinkUiEnabled"] = is_marketplace_affiliate_link_ui_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_revenue_split_tier import RobloxItemConfigurationApiRevenueSplitTier  # noqa: PLC0415
        from ..models.roblox_item_configuration_api_scheduled_publishing_settings import (
            RobloxItemConfigurationApiScheduledPublishingSettings,  # noqa: PLC0415
        )

        d = dict(src_dict)
        is_collectibles_controller_enabled = d.pop("isCollectiblesControllerEnabled", UNSET)

        is_collectibles_publishing_enabled = d.pop("isCollectiblesPublishingEnabled", UNSET)

        is_collectibles_publishing_location_type_enabled = d.pop("isCollectiblesPublishingLocationTypeEnabled", UNSET)

        _allowed_collectible_sale_locations = d.pop("allowedCollectibleSaleLocations", UNSET)
        allowed_collectible_sale_locations: (
            list[RobloxItemConfigurationApiCollectiblesMetadataResponseAllowedCollectibleSaleLocationsItem] | Unset
        ) = UNSET
        if _allowed_collectible_sale_locations is not UNSET:
            allowed_collectible_sale_locations = []
            for allowed_collectible_sale_locations_item_data in _allowed_collectible_sale_locations:
                allowed_collectible_sale_locations_item = (
                    RobloxItemConfigurationApiCollectiblesMetadataResponseAllowedCollectibleSaleLocationsItem(
                        allowed_collectible_sale_locations_item_data
                    )
                )

                allowed_collectible_sale_locations.append(allowed_collectible_sale_locations_item)

        is_collectible_free_item_publishing_available = d.pop("IsCollectibleFreeItemPublishingAvailable", UNSET)

        is_collectible_group_publishing_available = d.pop("isCollectibleGroupPublishingAvailable", UNSET)

        is_collectible_resale_restrictions_enabled = d.pop("isCollectibleResaleRestrictionsEnabled", UNSET)

        is_collectible_publish_min_quantity_enabled = d.pop("isCollectiblePublishMinQuantityEnabled", UNSET)

        is_ugc_4_all_ui_enabled = d.pop("IsUgc4AllUIEnabled", UNSET)

        limited_max_quantity = d.pop("LimitedMaxQuantity", UNSET)

        max_collectible_price = d.pop("MaxCollectiblePrice", UNSET)

        is_limited_collectible_bundles_publishing_enabled = d.pop("IsLimitedCollectibleBundlesPublishingEnabled", UNSET)

        is_resellability_enabled = d.pop("IsResellabilityEnabled", UNSET)

        is_new_bundle_ui_enabled = d.pop("IsNewBundleUIEnabled", UNSET)

        is_collectible_2d_publishing_enabled = d.pop("IsCollectible2DPublishingEnabled", UNSET)

        is_avatar_creation_tokens_ui_enabled = d.pop("IsAvatarCreationTokensUIEnabled", UNSET)

        is_scheduled_publishing_enabled = d.pop("IsScheduledPublishingEnabled", UNSET)

        _scheduled_publishing_settings = d.pop("ScheduledPublishingSettings", UNSET)
        scheduled_publishing_settings: RobloxItemConfigurationApiScheduledPublishingSettings | Unset
        if isinstance(_scheduled_publishing_settings, Unset):
            scheduled_publishing_settings = UNSET
        else:
            scheduled_publishing_settings = RobloxItemConfigurationApiScheduledPublishingSettings.from_dict(
                _scheduled_publishing_settings
            )

        is_get_price_floor_enabled = d.pop("isGetPriceFloorEnabled", UNSET)

        is_regional_pricing_enabled = d.pop("isRegionalPricingEnabled", UNSET)

        is_revenue_split_enabled = d.pop("isRevenueSplitEnabled", UNSET)

        _revenue_split_tiers_for_purchase = d.pop("revenueSplitTiersForPurchase", UNSET)
        revenue_split_tiers_for_purchase: list[RobloxItemConfigurationApiRevenueSplitTier] | Unset = UNSET
        if _revenue_split_tiers_for_purchase is not UNSET:
            revenue_split_tiers_for_purchase = []
            for revenue_split_tiers_for_purchase_item_data in _revenue_split_tiers_for_purchase:
                revenue_split_tiers_for_purchase_item = RobloxItemConfigurationApiRevenueSplitTier.from_dict(
                    revenue_split_tiers_for_purchase_item_data
                )

                revenue_split_tiers_for_purchase.append(revenue_split_tiers_for_purchase_item)

        is_content_metadata_appeal_enabled = d.pop("isContentMetadataAppealEnabled", UNSET)

        bodysuit_eligible_asset_types = cast(list[int], d.pop("bodysuitEligibleAssetTypes", UNSET))

        unify_configure_ui = d.pop("unifyConfigureUI", UNSET)

        is_restocking_enabled = d.pop("isRestockingEnabled", UNSET)

        restock_resale_lock_duration_seconds = d.pop("restockResaleLockDurationSeconds", UNSET)

        is_avatar_item_licensing_enabled = d.pop("isAvatarItemLicensingEnabled", UNSET)

        is_marketplace_affiliate_link_ui_enabled = d.pop("isMarketplaceAffiliateLinkUiEnabled", UNSET)

        roblox_item_configuration_api_collectibles_metadata_response = cls(
            is_collectibles_controller_enabled=is_collectibles_controller_enabled,
            is_collectibles_publishing_enabled=is_collectibles_publishing_enabled,
            is_collectibles_publishing_location_type_enabled=is_collectibles_publishing_location_type_enabled,
            allowed_collectible_sale_locations=allowed_collectible_sale_locations,
            is_collectible_free_item_publishing_available=is_collectible_free_item_publishing_available,
            is_collectible_group_publishing_available=is_collectible_group_publishing_available,
            is_collectible_resale_restrictions_enabled=is_collectible_resale_restrictions_enabled,
            is_collectible_publish_min_quantity_enabled=is_collectible_publish_min_quantity_enabled,
            is_ugc_4_all_ui_enabled=is_ugc_4_all_ui_enabled,
            limited_max_quantity=limited_max_quantity,
            max_collectible_price=max_collectible_price,
            is_limited_collectible_bundles_publishing_enabled=is_limited_collectible_bundles_publishing_enabled,
            is_resellability_enabled=is_resellability_enabled,
            is_new_bundle_ui_enabled=is_new_bundle_ui_enabled,
            is_collectible_2d_publishing_enabled=is_collectible_2d_publishing_enabled,
            is_avatar_creation_tokens_ui_enabled=is_avatar_creation_tokens_ui_enabled,
            is_scheduled_publishing_enabled=is_scheduled_publishing_enabled,
            scheduled_publishing_settings=scheduled_publishing_settings,
            is_get_price_floor_enabled=is_get_price_floor_enabled,
            is_regional_pricing_enabled=is_regional_pricing_enabled,
            is_revenue_split_enabled=is_revenue_split_enabled,
            revenue_split_tiers_for_purchase=revenue_split_tiers_for_purchase,
            is_content_metadata_appeal_enabled=is_content_metadata_appeal_enabled,
            bodysuit_eligible_asset_types=bodysuit_eligible_asset_types,
            unify_configure_ui=unify_configure_ui,
            is_restocking_enabled=is_restocking_enabled,
            restock_resale_lock_duration_seconds=restock_resale_lock_duration_seconds,
            is_avatar_item_licensing_enabled=is_avatar_item_licensing_enabled,
            is_marketplace_affiliate_link_ui_enabled=is_marketplace_affiliate_link_ui_enabled,
        )

        return roblox_item_configuration_api_collectibles_metadata_response
