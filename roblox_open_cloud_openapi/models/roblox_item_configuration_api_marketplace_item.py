from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_marketplace_item_cannot_be_published_reason import (
    RobloxItemConfigurationApiMarketplaceItemCannotBePublishedReason,
)
from ..models.roblox_item_configuration_api_marketplace_item_collectible_item_type import (
    RobloxItemConfigurationApiMarketplaceItemCollectibleItemType,
)
from ..models.roblox_item_configuration_api_marketplace_item_moderation_status import (
    RobloxItemConfigurationApiMarketplaceItemModerationStatus,
)
from ..models.roblox_item_configuration_api_marketplace_item_sale_status import (
    RobloxItemConfigurationApiMarketplaceItemSaleStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_dynamic_price_configuration import (
        RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1DynamicPriceConfiguration,
    )
    from ..models.roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_item_delisting_status import (
        RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatus,
    )
    from ..models.roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator import (
        RobloxAvatarMarketplacePublishingSharedV1Beta1Creator,
    )
    from ..models.roblox_collectibles_shared_v1_scheduled_release import RobloxCollectiblesSharedV1ScheduledRelease
    from ..models.roblox_item_configuration_api_marketplace_item_details import (
        RobloxItemConfigurationApiMarketplaceItemDetails,
    )
    from ..models.roblox_item_configuration_api_models_marketplace_item_collectible_details import (
        RobloxItemConfigurationApiModelsMarketplaceItemCollectibleDetails,
    )
    from ..models.roblox_item_configuration_api_models_marketplace_item_discoverability_details import (
        RobloxItemConfigurationApiModelsMarketplaceItemDiscoverabilityDetails,
    )
    from ..models.roblox_item_configuration_api_models_marketplace_item_sale_location import (
        RobloxItemConfigurationApiModelsMarketplaceItemSaleLocation,
    )
    from ..models.roblox_item_configuration_api_models_marketplace_item_taxonomy_details import (
        RobloxItemConfigurationApiModelsMarketplaceItemTaxonomyDetails,
    )
    from ..models.roblox_item_configuration_api_rental_option import RobloxItemConfigurationApiRentalOption


T = TypeVar("T", bound="RobloxItemConfigurationApiMarketplaceItem")


@_attrs_define
class RobloxItemConfigurationApiMarketplaceItem:
    """
    Attributes:
        id (str | Unset): The id of the item.
        marketplace_item_details (RobloxItemConfigurationApiMarketplaceItemDetails | Unset): The marketplace item
            details.
            Only one of the AssetDetails and BundleDetails will be set.
        created_time (datetime.datetime | Unset): The created time.
        name (str | Unset): The name of the item.
        description (str | Unset): The description of the item.
        creator (RobloxAvatarMarketplacePublishingSharedV1Beta1Creator | Unset):
        moderation_status (RobloxItemConfigurationApiMarketplaceItemModerationStatus | Unset): The moderation status of
            the item. ['Invalid' = 0, 'Pending' = 1, 'Moderated' = 2, 'Approved' = 3, 'RequiresIntervention' = 4]
        is_updating (bool | Unset): Whether the item currently has an in-flight Catalog Asset Update (a submitted update
            whose
            staging content is still being created / validated / moderated). The creator dashboard renders
            such an item as "pending" — the same treatment as an item still under moderation review.
        price (int | Unset): The price of the item.
            If price = 0 => free, if price = null => unset.
        sale_status (RobloxItemConfigurationApiMarketplaceItemSaleStatus | Unset): The sale status of the item.
            ['OnSale' = 0, 'OffSale' = 1, 'Free' = 2]
        collectible_item_type (RobloxItemConfigurationApiMarketplaceItemCollectibleItemType | Unset): The collectible
            item type.
            If null => item has not been published into collectible system. ['Invalid' = 0, 'Limited' = 1, 'NonLimited' = 2]
        creation_universe_id (int | Unset): The creation universe id.
            Used for IEC items.
        delisting_status (RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatus
            | Unset):
        scheduled_release (RobloxCollectiblesSharedV1ScheduledRelease | Unset):
        cannot_be_published_reason (RobloxItemConfigurationApiMarketplaceItemCannotBePublishedReason | Unset): The
            cannot be published reason.
            If Invalid, the item CAN be published. ['Invalid' = 0, 'None' = 1, 'Iec' = 2, 'AssetPartOfBundle' = 3,
            'Delisted' = 4, 'RealWorldCommerce' = 5, 'AiGenerated' = 6]
        dynamic_price_configuration
            (RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1DynamicPriceConfiguration | Unset):
        is_rental_opt_in (bool | Unset): Whether the item is opted into rental.
        rental_options (list[RobloxItemConfigurationApiRentalOption] | Unset): All rental options for the collectible
            item. Empty if the item is not opted in for rental.
        taxonomy_details (RobloxItemConfigurationApiModelsMarketplaceItemTaxonomyDetails | Unset): The taxonomy-related
            details of an item.
        is_hd (bool | Unset): Whether the item is HD.
        discoverability_details (RobloxItemConfigurationApiModelsMarketplaceItemDiscoverabilityDetails | Unset): The
            discoverability-related details of an item.
        is_emissive (bool | Unset): Whether the item has emissive properties.
        is_collectible (bool | Unset): Whether the item is a collectible (i.e. it has been published into the
            collectible system).
        sale_location (RobloxItemConfigurationApiModelsMarketplaceItemSaleLocation | Unset): The collectible sale
            location.
        collectible_details (RobloxItemConfigurationApiModelsMarketplaceItemCollectibleDetails | Unset): Details
            specific to a collectible item. Set only when the item is a collectible.
    """

    id: str | Unset = UNSET
    marketplace_item_details: RobloxItemConfigurationApiMarketplaceItemDetails | Unset = UNSET
    created_time: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    creator: RobloxAvatarMarketplacePublishingSharedV1Beta1Creator | Unset = UNSET
    moderation_status: RobloxItemConfigurationApiMarketplaceItemModerationStatus | Unset = UNSET
    is_updating: bool | Unset = UNSET
    price: int | Unset = UNSET
    sale_status: RobloxItemConfigurationApiMarketplaceItemSaleStatus | Unset = UNSET
    collectible_item_type: RobloxItemConfigurationApiMarketplaceItemCollectibleItemType | Unset = UNSET
    creation_universe_id: int | Unset = UNSET
    delisting_status: (
        RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatus | Unset
    ) = UNSET
    scheduled_release: RobloxCollectiblesSharedV1ScheduledRelease | Unset = UNSET
    cannot_be_published_reason: RobloxItemConfigurationApiMarketplaceItemCannotBePublishedReason | Unset = UNSET
    dynamic_price_configuration: (
        RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1DynamicPriceConfiguration | Unset
    ) = UNSET
    is_rental_opt_in: bool | Unset = UNSET
    rental_options: list[RobloxItemConfigurationApiRentalOption] | Unset = UNSET
    taxonomy_details: RobloxItemConfigurationApiModelsMarketplaceItemTaxonomyDetails | Unset = UNSET
    is_hd: bool | Unset = UNSET
    discoverability_details: RobloxItemConfigurationApiModelsMarketplaceItemDiscoverabilityDetails | Unset = UNSET
    is_emissive: bool | Unset = UNSET
    is_collectible: bool | Unset = UNSET
    sale_location: RobloxItemConfigurationApiModelsMarketplaceItemSaleLocation | Unset = UNSET
    collectible_details: RobloxItemConfigurationApiModelsMarketplaceItemCollectibleDetails | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        marketplace_item_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.marketplace_item_details, Unset):
            marketplace_item_details = self.marketplace_item_details.to_dict()

        created_time: str | Unset = UNSET
        if not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        name = self.name

        description = self.description

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        moderation_status: int | Unset = UNSET
        if not isinstance(self.moderation_status, Unset):
            moderation_status = self.moderation_status.value

        is_updating = self.is_updating

        price = self.price

        sale_status: int | Unset = UNSET
        if not isinstance(self.sale_status, Unset):
            sale_status = self.sale_status.value

        collectible_item_type: int | Unset = UNSET
        if not isinstance(self.collectible_item_type, Unset):
            collectible_item_type = self.collectible_item_type.value

        creation_universe_id = self.creation_universe_id

        delisting_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delisting_status, Unset):
            delisting_status = self.delisting_status.to_dict()

        scheduled_release: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scheduled_release, Unset):
            scheduled_release = self.scheduled_release.to_dict()

        cannot_be_published_reason: int | Unset = UNSET
        if not isinstance(self.cannot_be_published_reason, Unset):
            cannot_be_published_reason = self.cannot_be_published_reason.value

        dynamic_price_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_price_configuration, Unset):
            dynamic_price_configuration = self.dynamic_price_configuration.to_dict()

        is_rental_opt_in = self.is_rental_opt_in

        rental_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rental_options, Unset):
            rental_options = []
            for rental_options_item_data in self.rental_options:
                rental_options_item = rental_options_item_data.to_dict()
                rental_options.append(rental_options_item)

        taxonomy_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.taxonomy_details, Unset):
            taxonomy_details = self.taxonomy_details.to_dict()

        is_hd = self.is_hd

        discoverability_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discoverability_details, Unset):
            discoverability_details = self.discoverability_details.to_dict()

        is_emissive = self.is_emissive

        is_collectible = self.is_collectible

        sale_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sale_location, Unset):
            sale_location = self.sale_location.to_dict()

        collectible_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.collectible_details, Unset):
            collectible_details = self.collectible_details.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if marketplace_item_details is not UNSET:
            field_dict["marketplaceItemDetails"] = marketplace_item_details
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if creator is not UNSET:
            field_dict["creator"] = creator
        if moderation_status is not UNSET:
            field_dict["moderationStatus"] = moderation_status
        if is_updating is not UNSET:
            field_dict["isUpdating"] = is_updating
        if price is not UNSET:
            field_dict["price"] = price
        if sale_status is not UNSET:
            field_dict["saleStatus"] = sale_status
        if collectible_item_type is not UNSET:
            field_dict["collectibleItemType"] = collectible_item_type
        if creation_universe_id is not UNSET:
            field_dict["creationUniverseId"] = creation_universe_id
        if delisting_status is not UNSET:
            field_dict["delistingStatus"] = delisting_status
        if scheduled_release is not UNSET:
            field_dict["scheduledRelease"] = scheduled_release
        if cannot_be_published_reason is not UNSET:
            field_dict["cannotBePublishedReason"] = cannot_be_published_reason
        if dynamic_price_configuration is not UNSET:
            field_dict["dynamicPriceConfiguration"] = dynamic_price_configuration
        if is_rental_opt_in is not UNSET:
            field_dict["isRentalOptIn"] = is_rental_opt_in
        if rental_options is not UNSET:
            field_dict["rentalOptions"] = rental_options
        if taxonomy_details is not UNSET:
            field_dict["taxonomyDetails"] = taxonomy_details
        if is_hd is not UNSET:
            field_dict["isHD"] = is_hd
        if discoverability_details is not UNSET:
            field_dict["discoverabilityDetails"] = discoverability_details
        if is_emissive is not UNSET:
            field_dict["isEmissive"] = is_emissive
        if is_collectible is not UNSET:
            field_dict["isCollectible"] = is_collectible
        if sale_location is not UNSET:
            field_dict["saleLocation"] = sale_location
        if collectible_details is not UNSET:
            field_dict["collectibleDetails"] = collectible_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_dynamic_price_configuration import (
            RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1DynamicPriceConfiguration,  # noqa: PLC0415
        )
        from ..models.roblox_avatar_marketplace_publishing_avatar_marketplace_publishing_gateway_v1_beta_1_item_delisting_status import (
            RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatus,  # noqa: PLC0415
        )
        from ..models.roblox_avatar_marketplace_publishing_shared_v1_beta_1_creator import (
            RobloxAvatarMarketplacePublishingSharedV1Beta1Creator,  # noqa: PLC0415
        )
        from ..models.roblox_collectibles_shared_v1_scheduled_release import RobloxCollectiblesSharedV1ScheduledRelease  # noqa: PLC0415
        from ..models.roblox_item_configuration_api_marketplace_item_details import (
            RobloxItemConfigurationApiMarketplaceItemDetails,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_models_marketplace_item_collectible_details import (
            RobloxItemConfigurationApiModelsMarketplaceItemCollectibleDetails,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_models_marketplace_item_discoverability_details import (
            RobloxItemConfigurationApiModelsMarketplaceItemDiscoverabilityDetails,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_models_marketplace_item_sale_location import (
            RobloxItemConfigurationApiModelsMarketplaceItemSaleLocation,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_models_marketplace_item_taxonomy_details import (
            RobloxItemConfigurationApiModelsMarketplaceItemTaxonomyDetails,  # noqa: PLC0415
        )
        from ..models.roblox_item_configuration_api_rental_option import RobloxItemConfigurationApiRentalOption  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _marketplace_item_details = d.pop("marketplaceItemDetails", UNSET)
        marketplace_item_details: RobloxItemConfigurationApiMarketplaceItemDetails | Unset
        if isinstance(_marketplace_item_details, Unset):
            marketplace_item_details = UNSET
        else:
            marketplace_item_details = RobloxItemConfigurationApiMarketplaceItemDetails.from_dict(
                _marketplace_item_details
            )

        _created_time = d.pop("createdTime", UNSET)
        created_time: datetime.datetime | Unset
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = datetime.datetime.fromisoformat(_created_time)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: RobloxAvatarMarketplacePublishingSharedV1Beta1Creator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RobloxAvatarMarketplacePublishingSharedV1Beta1Creator.from_dict(_creator)

        _moderation_status = d.pop("moderationStatus", UNSET)
        moderation_status: RobloxItemConfigurationApiMarketplaceItemModerationStatus | Unset
        if isinstance(_moderation_status, Unset):
            moderation_status = UNSET
        else:
            moderation_status = RobloxItemConfigurationApiMarketplaceItemModerationStatus(_moderation_status)

        is_updating = d.pop("isUpdating", UNSET)

        price = d.pop("price", UNSET)

        _sale_status = d.pop("saleStatus", UNSET)
        sale_status: RobloxItemConfigurationApiMarketplaceItemSaleStatus | Unset
        if isinstance(_sale_status, Unset):
            sale_status = UNSET
        else:
            sale_status = RobloxItemConfigurationApiMarketplaceItemSaleStatus(_sale_status)

        _collectible_item_type = d.pop("collectibleItemType", UNSET)
        collectible_item_type: RobloxItemConfigurationApiMarketplaceItemCollectibleItemType | Unset
        if isinstance(_collectible_item_type, Unset):
            collectible_item_type = UNSET
        else:
            collectible_item_type = RobloxItemConfigurationApiMarketplaceItemCollectibleItemType(_collectible_item_type)

        creation_universe_id = d.pop("creationUniverseId", UNSET)

        _delisting_status = d.pop("delistingStatus", UNSET)
        delisting_status: (
            RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatus | Unset
        )
        if isinstance(_delisting_status, Unset):
            delisting_status = UNSET
        else:
            delisting_status = (
                RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1ItemDelistingStatus.from_dict(
                    _delisting_status
                )
            )

        _scheduled_release = d.pop("scheduledRelease", UNSET)
        scheduled_release: RobloxCollectiblesSharedV1ScheduledRelease | Unset
        if isinstance(_scheduled_release, Unset):
            scheduled_release = UNSET
        else:
            scheduled_release = RobloxCollectiblesSharedV1ScheduledRelease.from_dict(_scheduled_release)

        _cannot_be_published_reason = d.pop("cannotBePublishedReason", UNSET)
        cannot_be_published_reason: RobloxItemConfigurationApiMarketplaceItemCannotBePublishedReason | Unset
        if isinstance(_cannot_be_published_reason, Unset):
            cannot_be_published_reason = UNSET
        else:
            cannot_be_published_reason = RobloxItemConfigurationApiMarketplaceItemCannotBePublishedReason(
                _cannot_be_published_reason
            )

        _dynamic_price_configuration = d.pop("dynamicPriceConfiguration", UNSET)
        dynamic_price_configuration: (
            RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1DynamicPriceConfiguration | Unset
        )
        if isinstance(_dynamic_price_configuration, Unset):
            dynamic_price_configuration = UNSET
        else:
            dynamic_price_configuration = RobloxAvatarMarketplacePublishingAvatarMarketplacePublishingGatewayV1Beta1DynamicPriceConfiguration.from_dict(
                _dynamic_price_configuration
            )

        is_rental_opt_in = d.pop("isRentalOptIn", UNSET)

        _rental_options = d.pop("rentalOptions", UNSET)
        rental_options: list[RobloxItemConfigurationApiRentalOption] | Unset = UNSET
        if _rental_options is not UNSET:
            rental_options = []
            for rental_options_item_data in _rental_options:
                rental_options_item = RobloxItemConfigurationApiRentalOption.from_dict(rental_options_item_data)

                rental_options.append(rental_options_item)

        _taxonomy_details = d.pop("taxonomyDetails", UNSET)
        taxonomy_details: RobloxItemConfigurationApiModelsMarketplaceItemTaxonomyDetails | Unset
        if isinstance(_taxonomy_details, Unset):
            taxonomy_details = UNSET
        else:
            taxonomy_details = RobloxItemConfigurationApiModelsMarketplaceItemTaxonomyDetails.from_dict(
                _taxonomy_details
            )

        is_hd = d.pop("isHD", UNSET)

        _discoverability_details = d.pop("discoverabilityDetails", UNSET)
        discoverability_details: RobloxItemConfigurationApiModelsMarketplaceItemDiscoverabilityDetails | Unset
        if isinstance(_discoverability_details, Unset):
            discoverability_details = UNSET
        else:
            discoverability_details = RobloxItemConfigurationApiModelsMarketplaceItemDiscoverabilityDetails.from_dict(
                _discoverability_details
            )

        is_emissive = d.pop("isEmissive", UNSET)

        is_collectible = d.pop("isCollectible", UNSET)

        _sale_location = d.pop("saleLocation", UNSET)
        sale_location: RobloxItemConfigurationApiModelsMarketplaceItemSaleLocation | Unset
        if isinstance(_sale_location, Unset):
            sale_location = UNSET
        else:
            sale_location = RobloxItemConfigurationApiModelsMarketplaceItemSaleLocation.from_dict(_sale_location)

        _collectible_details = d.pop("collectibleDetails", UNSET)
        collectible_details: RobloxItemConfigurationApiModelsMarketplaceItemCollectibleDetails | Unset
        if isinstance(_collectible_details, Unset):
            collectible_details = UNSET
        else:
            collectible_details = RobloxItemConfigurationApiModelsMarketplaceItemCollectibleDetails.from_dict(
                _collectible_details
            )

        roblox_item_configuration_api_marketplace_item = cls(
            id=id,
            marketplace_item_details=marketplace_item_details,
            created_time=created_time,
            name=name,
            description=description,
            creator=creator,
            moderation_status=moderation_status,
            is_updating=is_updating,
            price=price,
            sale_status=sale_status,
            collectible_item_type=collectible_item_type,
            creation_universe_id=creation_universe_id,
            delisting_status=delisting_status,
            scheduled_release=scheduled_release,
            cannot_be_published_reason=cannot_be_published_reason,
            dynamic_price_configuration=dynamic_price_configuration,
            is_rental_opt_in=is_rental_opt_in,
            rental_options=rental_options,
            taxonomy_details=taxonomy_details,
            is_hd=is_hd,
            discoverability_details=discoverability_details,
            is_emissive=is_emissive,
            is_collectible=is_collectible,
            sale_location=sale_location,
            collectible_details=collectible_details,
        )

        return roblox_item_configuration_api_marketplace_item
