from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_catalog_search_detailed_response_item_v2_asset_type import (
    RobloxCatalogApiCatalogSearchDetailedResponseItemV2AssetType,
)
from ..models.roblox_catalog_api_catalog_search_detailed_response_item_v2_bundle_type import (
    RobloxCatalogApiCatalogSearchDetailedResponseItemV2BundleType,
)
from ..models.roblox_catalog_api_catalog_search_detailed_response_item_v2_creator_type import (
    RobloxCatalogApiCatalogSearchDetailedResponseItemV2CreatorType,
)
from ..models.roblox_catalog_api_catalog_search_detailed_response_item_v2_item_restrictions_item import (
    RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemRestrictionsItem,
)
from ..models.roblox_catalog_api_catalog_search_detailed_response_item_v2_item_status_item import (
    RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemStatusItem,
)
from ..models.roblox_catalog_api_catalog_search_detailed_response_item_v2_item_type import (
    RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemType,
)
from ..models.roblox_catalog_api_catalog_search_detailed_response_item_v2_sale_location_type import (
    RobloxCatalogApiCatalogSearchDetailedResponseItemV2SaleLocationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_bundle_item_detail_model_v2 import RobloxCatalogApiBundleItemDetailModelV2
    from ..models.roblox_catalog_api_discount_information import RobloxCatalogApiDiscountInformation
    from ..models.roblox_catalog_api_taxonomy_model import RobloxCatalogApiTaxonomyModel
    from ..models.roblox_catalog_api_timed_option import RobloxCatalogApiTimedOption


T = TypeVar("T", bound="RobloxCatalogApiCatalogSearchDetailedResponseItemV2")


@_attrs_define
class RobloxCatalogApiCatalogSearchDetailedResponseItemV2:
    """This is the beta (non game-engine) version of our hydration model representing asset or bundle in marketplace.

    Attributes:
        bundled_items (list[RobloxCatalogApiBundleItemDetailModelV2] | Unset): The
            System.Collections.Generic.IEnumerable`1 contained in the bundle, serialized if item is a bundle.
        taxonomy (list[RobloxCatalogApiTaxonomyModel] | Unset): The taxonomy ids and names for this item.
        item_created_utc (datetime.datetime | Unset): The UTC creation date-time of the asset or bundle.
        discount_information (RobloxCatalogApiDiscountInformation | Unset):
        id (int | Unset): The Item Id.
        item_type (RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemType | Unset): The
            Roblox.Catalog.Api.CatalogSearchDetailedResponseItem.ItemType item type. ['Asset' = 1, 'Bundle' = 2]
        asset_type (RobloxCatalogApiCatalogSearchDetailedResponseItemV2AssetType | Unset): The
            Roblox.Platform.Assets.AssetType serialized if item is an asset.
        bundle_type (RobloxCatalogApiCatalogSearchDetailedResponseItemV2BundleType | Unset): The
            Roblox.Platform.Bundles.Core.BundleType serialized if item is a bundle.
        is_recolorable (bool | Unset): Gets or sets the property whether a bundle is recolorable or not. Not serialized
            for asset.
        name (str | Unset): The item name.
        description (str | Unset): The item description.
        product_id (int | Unset): The product id of corresponding item.
        item_status (list[RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemStatusItem] | Unset): The
            System.Collections.Generic.IEnumerable`1 if item has Roblox.Catalog.Api.CatalogItemStatus.
        item_restrictions (list[RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemRestrictionsItem] | Unset): The
            System.Collections.Generic.IEnumerable`1 if item has Roblox.Catalog.Api.CatalogItemRestriction.
        creator_has_verified_badge (bool | Unset): The verified status of a creator.
        creator_type (RobloxCatalogApiCatalogSearchDetailedResponseItemV2CreatorType | Unset): The
            Roblox.Catalog.Api.CatalogSearchDetailedResponseItem.CreatorType of the item's creator.
        creator_target_id (int | Unset): The creator id of the item's creator.
        creator_name (str | Unset): The creator name of the item's creator.
        price (int | Unset): The item's price.
        lowest_price (int | Unset): The item's lowest price, only if the item is resellable and there are resellers.
        lowest_resale_price (int | Unset): The item's lowest resale price, only if the item is resellable and there are
            resellers, including current user.
        price_status (str | Unset): The localized string item status if the item's price should not be displayed.
        units_available_for_consumption (int | Unset): The number of items in stock, only if the item is resellable and
            is limitedEdition.
        favorite_count (int | Unset): The number of times the item has been favorited.
        off_sale_deadline (datetime.datetime | Unset): When the item will go off sale, if the item has an off deadline.
        collectible_item_id (str | Unset): The item's collectible item id.
            It is an UUID if a item is collectible type. Otherwise, it is null.
        total_quantity (int | Unset): The collectible or limited-unique item's total quantity of unique instances.
        sale_location_type (RobloxCatalogApiCatalogSearchDetailedResponseItemV2SaleLocationType | Unset): The sale
            location type of the item. ['NotApplicable' = 0, 'ShopOnly' = 1, 'MyExperiencesOnly' = 2, 'ShopAndMyExperiences'
            = 3, 'ExperiencesById' = 4, 'ShopAndAllExperiences' = 5, 'ExperiencesDevApiOnly' = 6, 'ShopAndExperiencesById' =
            7]
        has_resellers (bool | Unset): An indicator if the item has resellers or not (null if not resellable).
        is_off_sale (bool | Unset): An indicator if the item is off sale or not.
        quantity_limit_per_user (int | Unset): Quantity limit for how many instances a user can buy.
        supports_head_shapes (bool | Unset): Whether the item supports head shapes.
        timed_options (list[RobloxCatalogApiTimedOption] | Unset): The timed options for the item.
    """

    bundled_items: list[RobloxCatalogApiBundleItemDetailModelV2] | Unset = UNSET
    taxonomy: list[RobloxCatalogApiTaxonomyModel] | Unset = UNSET
    item_created_utc: datetime.datetime | Unset = UNSET
    discount_information: RobloxCatalogApiDiscountInformation | Unset = UNSET
    id: int | Unset = UNSET
    item_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemType | Unset = UNSET
    asset_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2AssetType | Unset = UNSET
    bundle_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2BundleType | Unset = UNSET
    is_recolorable: bool | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    product_id: int | Unset = UNSET
    item_status: list[RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemStatusItem] | Unset = UNSET
    item_restrictions: list[RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemRestrictionsItem] | Unset = UNSET
    creator_has_verified_badge: bool | Unset = UNSET
    creator_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2CreatorType | Unset = UNSET
    creator_target_id: int | Unset = UNSET
    creator_name: str | Unset = UNSET
    price: int | Unset = UNSET
    lowest_price: int | Unset = UNSET
    lowest_resale_price: int | Unset = UNSET
    price_status: str | Unset = UNSET
    units_available_for_consumption: int | Unset = UNSET
    favorite_count: int | Unset = UNSET
    off_sale_deadline: datetime.datetime | Unset = UNSET
    collectible_item_id: str | Unset = UNSET
    total_quantity: int | Unset = UNSET
    sale_location_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2SaleLocationType | Unset = UNSET
    has_resellers: bool | Unset = UNSET
    is_off_sale: bool | Unset = UNSET
    quantity_limit_per_user: int | Unset = UNSET
    supports_head_shapes: bool | Unset = UNSET
    timed_options: list[RobloxCatalogApiTimedOption] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bundled_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bundled_items, Unset):
            bundled_items = []
            for bundled_items_item_data in self.bundled_items:
                bundled_items_item = bundled_items_item_data.to_dict()
                bundled_items.append(bundled_items_item)

        taxonomy: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.taxonomy, Unset):
            taxonomy = []
            for taxonomy_item_data in self.taxonomy:
                taxonomy_item = taxonomy_item_data.to_dict()
                taxonomy.append(taxonomy_item)

        item_created_utc: str | Unset = UNSET
        if not isinstance(self.item_created_utc, Unset):
            item_created_utc = self.item_created_utc.isoformat()

        discount_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount_information, Unset):
            discount_information = self.discount_information.to_dict()

        id = self.id

        item_type: int | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        asset_type: int | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.value

        bundle_type: int | Unset = UNSET
        if not isinstance(self.bundle_type, Unset):
            bundle_type = self.bundle_type.value

        is_recolorable = self.is_recolorable

        name = self.name

        description = self.description

        product_id = self.product_id

        item_status: list[int] | Unset = UNSET
        if not isinstance(self.item_status, Unset):
            item_status = []
            for item_status_item_data in self.item_status:
                item_status_item = item_status_item_data.value
                item_status.append(item_status_item)

        item_restrictions: list[int] | Unset = UNSET
        if not isinstance(self.item_restrictions, Unset):
            item_restrictions = []
            for item_restrictions_item_data in self.item_restrictions:
                item_restrictions_item = item_restrictions_item_data.value
                item_restrictions.append(item_restrictions_item)

        creator_has_verified_badge = self.creator_has_verified_badge

        creator_type: int | Unset = UNSET
        if not isinstance(self.creator_type, Unset):
            creator_type = self.creator_type.value

        creator_target_id = self.creator_target_id

        creator_name = self.creator_name

        price = self.price

        lowest_price = self.lowest_price

        lowest_resale_price = self.lowest_resale_price

        price_status = self.price_status

        units_available_for_consumption = self.units_available_for_consumption

        favorite_count = self.favorite_count

        off_sale_deadline: str | Unset = UNSET
        if not isinstance(self.off_sale_deadline, Unset):
            off_sale_deadline = self.off_sale_deadline.isoformat()

        collectible_item_id = self.collectible_item_id

        total_quantity = self.total_quantity

        sale_location_type: int | Unset = UNSET
        if not isinstance(self.sale_location_type, Unset):
            sale_location_type = self.sale_location_type.value

        has_resellers = self.has_resellers

        is_off_sale = self.is_off_sale

        quantity_limit_per_user = self.quantity_limit_per_user

        supports_head_shapes = self.supports_head_shapes

        timed_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timed_options, Unset):
            timed_options = []
            for timed_options_item_data in self.timed_options:
                timed_options_item = timed_options_item_data.to_dict()
                timed_options.append(timed_options_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bundled_items is not UNSET:
            field_dict["bundledItems"] = bundled_items
        if taxonomy is not UNSET:
            field_dict["taxonomy"] = taxonomy
        if item_created_utc is not UNSET:
            field_dict["itemCreatedUtc"] = item_created_utc
        if discount_information is not UNSET:
            field_dict["discountInformation"] = discount_information
        if id is not UNSET:
            field_dict["id"] = id
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if asset_type is not UNSET:
            field_dict["assetType"] = asset_type
        if bundle_type is not UNSET:
            field_dict["bundleType"] = bundle_type
        if is_recolorable is not UNSET:
            field_dict["isRecolorable"] = is_recolorable
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if item_status is not UNSET:
            field_dict["itemStatus"] = item_status
        if item_restrictions is not UNSET:
            field_dict["itemRestrictions"] = item_restrictions
        if creator_has_verified_badge is not UNSET:
            field_dict["creatorHasVerifiedBadge"] = creator_has_verified_badge
        if creator_type is not UNSET:
            field_dict["creatorType"] = creator_type
        if creator_target_id is not UNSET:
            field_dict["creatorTargetId"] = creator_target_id
        if creator_name is not UNSET:
            field_dict["creatorName"] = creator_name
        if price is not UNSET:
            field_dict["price"] = price
        if lowest_price is not UNSET:
            field_dict["lowestPrice"] = lowest_price
        if lowest_resale_price is not UNSET:
            field_dict["lowestResalePrice"] = lowest_resale_price
        if price_status is not UNSET:
            field_dict["priceStatus"] = price_status
        if units_available_for_consumption is not UNSET:
            field_dict["unitsAvailableForConsumption"] = units_available_for_consumption
        if favorite_count is not UNSET:
            field_dict["favoriteCount"] = favorite_count
        if off_sale_deadline is not UNSET:
            field_dict["offSaleDeadline"] = off_sale_deadline
        if collectible_item_id is not UNSET:
            field_dict["collectibleItemId"] = collectible_item_id
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity
        if sale_location_type is not UNSET:
            field_dict["saleLocationType"] = sale_location_type
        if has_resellers is not UNSET:
            field_dict["hasResellers"] = has_resellers
        if is_off_sale is not UNSET:
            field_dict["isOffSale"] = is_off_sale
        if quantity_limit_per_user is not UNSET:
            field_dict["quantityLimitPerUser"] = quantity_limit_per_user
        if supports_head_shapes is not UNSET:
            field_dict["supportsHeadShapes"] = supports_head_shapes
        if timed_options is not UNSET:
            field_dict["timedOptions"] = timed_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_bundle_item_detail_model_v2 import RobloxCatalogApiBundleItemDetailModelV2
        from ..models.roblox_catalog_api_discount_information import RobloxCatalogApiDiscountInformation
        from ..models.roblox_catalog_api_taxonomy_model import RobloxCatalogApiTaxonomyModel
        from ..models.roblox_catalog_api_timed_option import RobloxCatalogApiTimedOption

        d = dict(src_dict)
        _bundled_items = d.pop("bundledItems", UNSET)
        bundled_items: list[RobloxCatalogApiBundleItemDetailModelV2] | Unset = UNSET
        if _bundled_items is not UNSET:
            bundled_items = []
            for bundled_items_item_data in _bundled_items:
                bundled_items_item = RobloxCatalogApiBundleItemDetailModelV2.from_dict(bundled_items_item_data)

                bundled_items.append(bundled_items_item)

        _taxonomy = d.pop("taxonomy", UNSET)
        taxonomy: list[RobloxCatalogApiTaxonomyModel] | Unset = UNSET
        if _taxonomy is not UNSET:
            taxonomy = []
            for taxonomy_item_data in _taxonomy:
                taxonomy_item = RobloxCatalogApiTaxonomyModel.from_dict(taxonomy_item_data)

                taxonomy.append(taxonomy_item)

        _item_created_utc = d.pop("itemCreatedUtc", UNSET)
        item_created_utc: datetime.datetime | Unset
        if isinstance(_item_created_utc, Unset):
            item_created_utc = UNSET
        else:
            item_created_utc = datetime.datetime.fromisoformat(_item_created_utc)

        _discount_information = d.pop("discountInformation", UNSET)
        discount_information: RobloxCatalogApiDiscountInformation | Unset
        if isinstance(_discount_information, Unset):
            discount_information = UNSET
        else:
            discount_information = RobloxCatalogApiDiscountInformation.from_dict(_discount_information)

        id = d.pop("id", UNSET)

        _item_type = d.pop("itemType", UNSET)
        item_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemType | Unset
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemType(_item_type)

        _asset_type = d.pop("assetType", UNSET)
        asset_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2AssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = RobloxCatalogApiCatalogSearchDetailedResponseItemV2AssetType(_asset_type)

        _bundle_type = d.pop("bundleType", UNSET)
        bundle_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2BundleType | Unset
        if isinstance(_bundle_type, Unset):
            bundle_type = UNSET
        else:
            bundle_type = RobloxCatalogApiCatalogSearchDetailedResponseItemV2BundleType(_bundle_type)

        is_recolorable = d.pop("isRecolorable", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        product_id = d.pop("productId", UNSET)

        _item_status = d.pop("itemStatus", UNSET)
        item_status: list[RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemStatusItem] | Unset = UNSET
        if _item_status is not UNSET:
            item_status = []
            for item_status_item_data in _item_status:
                item_status_item = RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemStatusItem(
                    item_status_item_data
                )

                item_status.append(item_status_item)

        _item_restrictions = d.pop("itemRestrictions", UNSET)
        item_restrictions: list[RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemRestrictionsItem] | Unset = UNSET
        if _item_restrictions is not UNSET:
            item_restrictions = []
            for item_restrictions_item_data in _item_restrictions:
                item_restrictions_item = RobloxCatalogApiCatalogSearchDetailedResponseItemV2ItemRestrictionsItem(
                    item_restrictions_item_data
                )

                item_restrictions.append(item_restrictions_item)

        creator_has_verified_badge = d.pop("creatorHasVerifiedBadge", UNSET)

        _creator_type = d.pop("creatorType", UNSET)
        creator_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2CreatorType | Unset
        if isinstance(_creator_type, Unset):
            creator_type = UNSET
        else:
            creator_type = RobloxCatalogApiCatalogSearchDetailedResponseItemV2CreatorType(_creator_type)

        creator_target_id = d.pop("creatorTargetId", UNSET)

        creator_name = d.pop("creatorName", UNSET)

        price = d.pop("price", UNSET)

        lowest_price = d.pop("lowestPrice", UNSET)

        lowest_resale_price = d.pop("lowestResalePrice", UNSET)

        price_status = d.pop("priceStatus", UNSET)

        units_available_for_consumption = d.pop("unitsAvailableForConsumption", UNSET)

        favorite_count = d.pop("favoriteCount", UNSET)

        _off_sale_deadline = d.pop("offSaleDeadline", UNSET)
        off_sale_deadline: datetime.datetime | Unset
        if isinstance(_off_sale_deadline, Unset):
            off_sale_deadline = UNSET
        else:
            off_sale_deadline = datetime.datetime.fromisoformat(_off_sale_deadline)

        collectible_item_id = d.pop("collectibleItemId", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        _sale_location_type = d.pop("saleLocationType", UNSET)
        sale_location_type: RobloxCatalogApiCatalogSearchDetailedResponseItemV2SaleLocationType | Unset
        if isinstance(_sale_location_type, Unset):
            sale_location_type = UNSET
        else:
            sale_location_type = RobloxCatalogApiCatalogSearchDetailedResponseItemV2SaleLocationType(
                _sale_location_type
            )

        has_resellers = d.pop("hasResellers", UNSET)

        is_off_sale = d.pop("isOffSale", UNSET)

        quantity_limit_per_user = d.pop("quantityLimitPerUser", UNSET)

        supports_head_shapes = d.pop("supportsHeadShapes", UNSET)

        _timed_options = d.pop("timedOptions", UNSET)
        timed_options: list[RobloxCatalogApiTimedOption] | Unset = UNSET
        if _timed_options is not UNSET:
            timed_options = []
            for timed_options_item_data in _timed_options:
                timed_options_item = RobloxCatalogApiTimedOption.from_dict(timed_options_item_data)

                timed_options.append(timed_options_item)

        roblox_catalog_api_catalog_search_detailed_response_item_v2 = cls(
            bundled_items=bundled_items,
            taxonomy=taxonomy,
            item_created_utc=item_created_utc,
            discount_information=discount_information,
            id=id,
            item_type=item_type,
            asset_type=asset_type,
            bundle_type=bundle_type,
            is_recolorable=is_recolorable,
            name=name,
            description=description,
            product_id=product_id,
            item_status=item_status,
            item_restrictions=item_restrictions,
            creator_has_verified_badge=creator_has_verified_badge,
            creator_type=creator_type,
            creator_target_id=creator_target_id,
            creator_name=creator_name,
            price=price,
            lowest_price=lowest_price,
            lowest_resale_price=lowest_resale_price,
            price_status=price_status,
            units_available_for_consumption=units_available_for_consumption,
            favorite_count=favorite_count,
            off_sale_deadline=off_sale_deadline,
            collectible_item_id=collectible_item_id,
            total_quantity=total_quantity,
            sale_location_type=sale_location_type,
            has_resellers=has_resellers,
            is_off_sale=is_off_sale,
            quantity_limit_per_user=quantity_limit_per_user,
            supports_head_shapes=supports_head_shapes,
            timed_options=timed_options,
        )

        return roblox_catalog_api_catalog_search_detailed_response_item_v2
