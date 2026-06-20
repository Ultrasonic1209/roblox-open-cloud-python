from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiTaxonomyModel")


@_attrs_define
class RobloxCatalogApiTaxonomyModel:
    """public api model coaslescing taxonomy information for a single item.

    Attributes:
        taxonomy_id (str | Unset): The id value to pass into taxonomy field in SearchV2 catalog-api.
        taxonomy_name (str | Unset): The localized human readable name of the category.
    """

    taxonomy_id: str | Unset = UNSET
    taxonomy_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        taxonomy_id = self.taxonomy_id

        taxonomy_name = self.taxonomy_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if taxonomy_id is not UNSET:
            field_dict["taxonomyId"] = taxonomy_id
        if taxonomy_name is not UNSET:
            field_dict["taxonomyName"] = taxonomy_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        taxonomy_id = d.pop("taxonomyId", UNSET)

        taxonomy_name = d.pop("taxonomyName", UNSET)

        roblox_catalog_api_taxonomy_model = cls(
            taxonomy_id=taxonomy_id,
            taxonomy_name=taxonomy_name,
        )

        return roblox_catalog_api_taxonomy_model
