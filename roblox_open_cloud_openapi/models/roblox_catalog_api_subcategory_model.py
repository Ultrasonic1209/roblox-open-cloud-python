from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_subcategory_model_subcategory import RobloxCatalogApiSubcategoryModelSubcategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiSubcategoryModel")


@_attrs_define
class RobloxCatalogApiSubcategoryModel:
    """Response model for subcategory.

    Attributes:
        subcategory (RobloxCatalogApiSubcategoryModelSubcategory | Unset): Subcategory type.
        taxonomy (str | Unset): The taxonomy UUID associated with this node.
        asset_type_ids (list[int] | Unset): List of AssetTypeIds corresponding to AssetType enum that this category
            returns.
        bundle_type_ids (list[int] | Unset): List of bundleTypeIds corresponding to BundleType enum that this category
            returns.
        subcategory_id (int | Unset): Subcategory id.
        name (str | Unset): Subcategory name.
        short_name (str | Unset): Subcategory short name.
    """

    subcategory: RobloxCatalogApiSubcategoryModelSubcategory | Unset = UNSET
    taxonomy: str | Unset = UNSET
    asset_type_ids: list[int] | Unset = UNSET
    bundle_type_ids: list[int] | Unset = UNSET
    subcategory_id: int | Unset = UNSET
    name: str | Unset = UNSET
    short_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subcategory: int | Unset = UNSET
        if not isinstance(self.subcategory, Unset):
            subcategory = self.subcategory.value

        taxonomy = self.taxonomy

        asset_type_ids: list[int] | Unset = UNSET
        if not isinstance(self.asset_type_ids, Unset):
            asset_type_ids = self.asset_type_ids

        bundle_type_ids: list[int] | Unset = UNSET
        if not isinstance(self.bundle_type_ids, Unset):
            bundle_type_ids = self.bundle_type_ids

        subcategory_id = self.subcategory_id

        name = self.name

        short_name = self.short_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if taxonomy is not UNSET:
            field_dict["taxonomy"] = taxonomy
        if asset_type_ids is not UNSET:
            field_dict["assetTypeIds"] = asset_type_ids
        if bundle_type_ids is not UNSET:
            field_dict["bundleTypeIds"] = bundle_type_ids
        if subcategory_id is not UNSET:
            field_dict["subcategoryId"] = subcategory_id
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _subcategory = d.pop("subcategory", UNSET)
        subcategory: RobloxCatalogApiSubcategoryModelSubcategory | Unset
        if isinstance(_subcategory, Unset):
            subcategory = UNSET
        else:
            subcategory = RobloxCatalogApiSubcategoryModelSubcategory(_subcategory)

        taxonomy = d.pop("taxonomy", UNSET)

        asset_type_ids = cast(list[int], d.pop("assetTypeIds", UNSET))

        bundle_type_ids = cast(list[int], d.pop("bundleTypeIds", UNSET))

        subcategory_id = d.pop("subcategoryId", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        roblox_catalog_api_subcategory_model = cls(
            subcategory=subcategory,
            taxonomy=taxonomy,
            asset_type_ids=asset_type_ids,
            bundle_type_ids=bundle_type_ids,
            subcategory_id=subcategory_id,
            name=name,
            short_name=short_name,
        )

        return roblox_catalog_api_subcategory_model
