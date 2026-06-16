from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_bundle_details_model_item_restrictions_item import (
    RobloxCatalogApiBundleDetailsModelItemRestrictionsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_bundle_creator_model import RobloxCatalogApiBundleCreatorModel
    from ..models.roblox_catalog_api_bundle_item_detail_model import RobloxCatalogApiBundleItemDetailModel
    from ..models.roblox_catalog_api_bundle_product_model import RobloxCatalogApiBundleProductModel
    from ..models.roblox_catalog_api_collectible_item_detail import RobloxCatalogApiCollectibleItemDetail
    from ..models.roblox_catalog_api_discount_information import RobloxCatalogApiDiscountInformation


T = TypeVar("T", bound="RobloxCatalogApiBundleDetailsModel")


@_attrs_define
class RobloxCatalogApiBundleDetailsModel:
    """The hydration model representing a bundle on marketplace. Returned in all bundles controller endpoints.
    Bound in the game-engine MarketplaceService.GetProductInfo method.
    https://create.roblox.com/docs/reference/engine/classes/MarketplaceService#GetProductInfo.

        Attributes:
            id (int | Unset):
            name (str | Unset):
            description (str | Unset):
            bundle_type (str | Unset):
            is_recolorable (bool | Unset):
            items (list[RobloxCatalogApiBundleItemDetailModel] | Unset):
            creator (RobloxCatalogApiBundleCreatorModel | Unset):
            product (RobloxCatalogApiBundleProductModel | Unset):
            item_restrictions (list[RobloxCatalogApiBundleDetailsModelItemRestrictionsItem] | Unset):
            collectible_item_detail (RobloxCatalogApiCollectibleItemDetail | Unset):
            discount_information (RobloxCatalogApiDiscountInformation | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    bundle_type: str | Unset = UNSET
    is_recolorable: bool | Unset = UNSET
    items: list[RobloxCatalogApiBundleItemDetailModel] | Unset = UNSET
    creator: RobloxCatalogApiBundleCreatorModel | Unset = UNSET
    product: RobloxCatalogApiBundleProductModel | Unset = UNSET
    item_restrictions: list[RobloxCatalogApiBundleDetailsModelItemRestrictionsItem] | Unset = UNSET
    collectible_item_detail: RobloxCatalogApiCollectibleItemDetail | Unset = UNSET
    discount_information: RobloxCatalogApiDiscountInformation | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        bundle_type = self.bundle_type

        is_recolorable = self.is_recolorable

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        item_restrictions: list[int] | Unset = UNSET
        if not isinstance(self.item_restrictions, Unset):
            item_restrictions = []
            for item_restrictions_item_data in self.item_restrictions:
                item_restrictions_item = item_restrictions_item_data.value
                item_restrictions.append(item_restrictions_item)

        collectible_item_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.collectible_item_detail, Unset):
            collectible_item_detail = self.collectible_item_detail.to_dict()

        discount_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount_information, Unset):
            discount_information = self.discount_information.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if bundle_type is not UNSET:
            field_dict["bundleType"] = bundle_type
        if is_recolorable is not UNSET:
            field_dict["isRecolorable"] = is_recolorable
        if items is not UNSET:
            field_dict["items"] = items
        if creator is not UNSET:
            field_dict["creator"] = creator
        if product is not UNSET:
            field_dict["product"] = product
        if item_restrictions is not UNSET:
            field_dict["itemRestrictions"] = item_restrictions
        if collectible_item_detail is not UNSET:
            field_dict["collectibleItemDetail"] = collectible_item_detail
        if discount_information is not UNSET:
            field_dict["discountInformation"] = discount_information

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_bundle_creator_model import RobloxCatalogApiBundleCreatorModel
        from ..models.roblox_catalog_api_bundle_item_detail_model import RobloxCatalogApiBundleItemDetailModel
        from ..models.roblox_catalog_api_bundle_product_model import RobloxCatalogApiBundleProductModel
        from ..models.roblox_catalog_api_collectible_item_detail import RobloxCatalogApiCollectibleItemDetail
        from ..models.roblox_catalog_api_discount_information import RobloxCatalogApiDiscountInformation

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        bundle_type = d.pop("bundleType", UNSET)

        is_recolorable = d.pop("isRecolorable", UNSET)

        _items = d.pop("items", UNSET)
        items: list[RobloxCatalogApiBundleItemDetailModel] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RobloxCatalogApiBundleItemDetailModel.from_dict(items_item_data)

                items.append(items_item)

        _creator = d.pop("creator", UNSET)
        creator: RobloxCatalogApiBundleCreatorModel | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RobloxCatalogApiBundleCreatorModel.from_dict(_creator)

        _product = d.pop("product", UNSET)
        product: RobloxCatalogApiBundleProductModel | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = RobloxCatalogApiBundleProductModel.from_dict(_product)

        _item_restrictions = d.pop("itemRestrictions", UNSET)
        item_restrictions: list[RobloxCatalogApiBundleDetailsModelItemRestrictionsItem] | Unset = UNSET
        if _item_restrictions is not UNSET:
            item_restrictions = []
            for item_restrictions_item_data in _item_restrictions:
                item_restrictions_item = RobloxCatalogApiBundleDetailsModelItemRestrictionsItem(
                    item_restrictions_item_data
                )

                item_restrictions.append(item_restrictions_item)

        _collectible_item_detail = d.pop("collectibleItemDetail", UNSET)
        collectible_item_detail: RobloxCatalogApiCollectibleItemDetail | Unset
        if isinstance(_collectible_item_detail, Unset):
            collectible_item_detail = UNSET
        else:
            collectible_item_detail = RobloxCatalogApiCollectibleItemDetail.from_dict(_collectible_item_detail)

        _discount_information = d.pop("discountInformation", UNSET)
        discount_information: RobloxCatalogApiDiscountInformation | Unset
        if isinstance(_discount_information, Unset):
            discount_information = UNSET
        else:
            discount_information = RobloxCatalogApiDiscountInformation.from_dict(_discount_information)

        roblox_catalog_api_bundle_details_model = cls(
            id=id,
            name=name,
            description=description,
            bundle_type=bundle_type,
            is_recolorable=is_recolorable,
            items=items,
            creator=creator,
            product=product,
            item_restrictions=item_restrictions,
            collectible_item_detail=collectible_item_detail,
            discount_information=discount_information,
        )

        return roblox_catalog_api_bundle_details_model
