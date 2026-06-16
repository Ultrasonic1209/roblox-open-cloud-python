from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_category_model_category import RobloxCatalogApiCategoryModelCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_subcategory_model import RobloxCatalogApiSubcategoryModel


T = TypeVar("T", bound="RobloxCatalogApiCategoryModel")


@_attrs_define
class RobloxCatalogApiCategoryModel:
    """Response model for category.

    Attributes:
        category (RobloxCatalogApiCategoryModelCategory | Unset): Category type.
        taxonomy (str | Unset): The associated public facing web_stable_id corresponding to internal taxonomy uuid for
            this category.
        asset_type_ids (list[int] | Unset): List of AssetTypeIds corresponding to AssetType enum that this category
            returns.
        bundle_type_ids (list[int] | Unset): List of bundleTypeIds corresponding to BundleType enum that this category
            returns.
        category_id (int | Unset): Category id.
        name (str | Unset): Category name.
        order_index (int | Unset): Category order index.
        subcategories (list[RobloxCatalogApiSubcategoryModel] | Unset): Subcategories under this category.
        is_searchable (bool | Unset): Gets or sets whether the category is searchable in search bar.
    """

    category: RobloxCatalogApiCategoryModelCategory | Unset = UNSET
    taxonomy: str | Unset = UNSET
    asset_type_ids: list[int] | Unset = UNSET
    bundle_type_ids: list[int] | Unset = UNSET
    category_id: int | Unset = UNSET
    name: str | Unset = UNSET
    order_index: int | Unset = UNSET
    subcategories: list[RobloxCatalogApiSubcategoryModel] | Unset = UNSET
    is_searchable: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category: int | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        taxonomy = self.taxonomy

        asset_type_ids: list[int] | Unset = UNSET
        if not isinstance(self.asset_type_ids, Unset):
            asset_type_ids = self.asset_type_ids

        bundle_type_ids: list[int] | Unset = UNSET
        if not isinstance(self.bundle_type_ids, Unset):
            bundle_type_ids = self.bundle_type_ids

        category_id = self.category_id

        name = self.name

        order_index = self.order_index

        subcategories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subcategories, Unset):
            subcategories = []
            for subcategories_item_data in self.subcategories:
                subcategories_item = subcategories_item_data.to_dict()
                subcategories.append(subcategories_item)

        is_searchable = self.is_searchable

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if taxonomy is not UNSET:
            field_dict["taxonomy"] = taxonomy
        if asset_type_ids is not UNSET:
            field_dict["assetTypeIds"] = asset_type_ids
        if bundle_type_ids is not UNSET:
            field_dict["bundleTypeIds"] = bundle_type_ids
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if name is not UNSET:
            field_dict["name"] = name
        if order_index is not UNSET:
            field_dict["orderIndex"] = order_index
        if subcategories is not UNSET:
            field_dict["subcategories"] = subcategories
        if is_searchable is not UNSET:
            field_dict["isSearchable"] = is_searchable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_subcategory_model import RobloxCatalogApiSubcategoryModel

        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: RobloxCatalogApiCategoryModelCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = RobloxCatalogApiCategoryModelCategory(_category)

        taxonomy = d.pop("taxonomy", UNSET)

        asset_type_ids = cast(list[int], d.pop("assetTypeIds", UNSET))

        bundle_type_ids = cast(list[int], d.pop("bundleTypeIds", UNSET))

        category_id = d.pop("categoryId", UNSET)

        name = d.pop("name", UNSET)

        order_index = d.pop("orderIndex", UNSET)

        _subcategories = d.pop("subcategories", UNSET)
        subcategories: list[RobloxCatalogApiSubcategoryModel] | Unset = UNSET
        if _subcategories is not UNSET:
            subcategories = []
            for subcategories_item_data in _subcategories:
                subcategories_item = RobloxCatalogApiSubcategoryModel.from_dict(subcategories_item_data)

                subcategories.append(subcategories_item)

        is_searchable = d.pop("isSearchable", UNSET)

        roblox_catalog_api_category_model = cls(
            category=category,
            taxonomy=taxonomy,
            asset_type_ids=asset_type_ids,
            bundle_type_ids=bundle_type_ids,
            category_id=category_id,
            name=name,
            order_index=order_index,
            subcategories=subcategories,
            is_searchable=is_searchable,
        )

        return roblox_catalog_api_category_model
