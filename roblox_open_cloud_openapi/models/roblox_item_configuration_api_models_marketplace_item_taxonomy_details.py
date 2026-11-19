from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsMarketplaceItemTaxonomyDetails")


@_attrs_define
class RobloxItemConfigurationApiModelsMarketplaceItemTaxonomyDetails:
    """The taxonomy-related details of an item.

    Attributes:
        dpf_taxonomy_name (str | Unset):
        dpf_taxonomy_id (str | Unset):
        dpf_taxonomy_is_default_taxonomy (bool | Unset):
    """

    dpf_taxonomy_name: str | Unset = UNSET
    dpf_taxonomy_id: str | Unset = UNSET
    dpf_taxonomy_is_default_taxonomy: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dpf_taxonomy_name = self.dpf_taxonomy_name

        dpf_taxonomy_id = self.dpf_taxonomy_id

        dpf_taxonomy_is_default_taxonomy = self.dpf_taxonomy_is_default_taxonomy

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dpf_taxonomy_name is not UNSET:
            field_dict["dpfTaxonomyName"] = dpf_taxonomy_name
        if dpf_taxonomy_id is not UNSET:
            field_dict["dpfTaxonomyId"] = dpf_taxonomy_id
        if dpf_taxonomy_is_default_taxonomy is not UNSET:
            field_dict["dpfTaxonomyIsDefaultTaxonomy"] = dpf_taxonomy_is_default_taxonomy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dpf_taxonomy_name = d.pop("dpfTaxonomyName", UNSET)

        dpf_taxonomy_id = d.pop("dpfTaxonomyId", UNSET)

        dpf_taxonomy_is_default_taxonomy = d.pop("dpfTaxonomyIsDefaultTaxonomy", UNSET)

        roblox_item_configuration_api_models_marketplace_item_taxonomy_details = cls(
            dpf_taxonomy_name=dpf_taxonomy_name,
            dpf_taxonomy_id=dpf_taxonomy_id,
            dpf_taxonomy_is_default_taxonomy=dpf_taxonomy_is_default_taxonomy,
        )

        return roblox_item_configuration_api_models_marketplace_item_taxonomy_details
