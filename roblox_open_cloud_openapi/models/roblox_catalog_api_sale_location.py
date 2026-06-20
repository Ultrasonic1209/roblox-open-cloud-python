from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_sale_location_sale_location_type import RobloxCatalogApiSaleLocationSaleLocationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiSaleLocation")


@_attrs_define
class RobloxCatalogApiSaleLocation:
    """SaleLocation information for a collectible item (asset or bundle).

    Attributes:
        sale_location_type (RobloxCatalogApiSaleLocationSaleLocationType | Unset): Sale location type related for an
            item detail. ['NotApplicable' = 0, 'ShopOnly' = 1, 'MyExperiencesOnly' = 2, 'ShopAndMyExperiences' = 3,
            'ExperiencesById' = 4, 'ShopAndAllExperiences' = 5, 'ExperiencesDevApiOnly' = 6, 'ShopAndExperiencesById' = 7]
        sale_location_type_id (int | Unset):
        universe_ids (list[int] | Unset):
        enabled_universe_ids (list[int] | Unset):
    """

    sale_location_type: RobloxCatalogApiSaleLocationSaleLocationType | Unset = UNSET
    sale_location_type_id: int | Unset = UNSET
    universe_ids: list[int] | Unset = UNSET
    enabled_universe_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sale_location_type: int | Unset = UNSET
        if not isinstance(self.sale_location_type, Unset):
            sale_location_type = self.sale_location_type.value

        sale_location_type_id = self.sale_location_type_id

        universe_ids: list[int] | Unset = UNSET
        if not isinstance(self.universe_ids, Unset):
            universe_ids = self.universe_ids

        enabled_universe_ids: list[int] | Unset = UNSET
        if not isinstance(self.enabled_universe_ids, Unset):
            enabled_universe_ids = self.enabled_universe_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sale_location_type is not UNSET:
            field_dict["saleLocationType"] = sale_location_type
        if sale_location_type_id is not UNSET:
            field_dict["saleLocationTypeId"] = sale_location_type_id
        if universe_ids is not UNSET:
            field_dict["universeIds"] = universe_ids
        if enabled_universe_ids is not UNSET:
            field_dict["enabledUniverseIds"] = enabled_universe_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _sale_location_type = d.pop("saleLocationType", UNSET)
        sale_location_type: RobloxCatalogApiSaleLocationSaleLocationType | Unset
        if isinstance(_sale_location_type, Unset):
            sale_location_type = UNSET
        else:
            sale_location_type = RobloxCatalogApiSaleLocationSaleLocationType(_sale_location_type)

        sale_location_type_id = d.pop("saleLocationTypeId", UNSET)

        universe_ids = cast(list[int], d.pop("universeIds", UNSET))

        enabled_universe_ids = cast(list[int], d.pop("enabledUniverseIds", UNSET))

        roblox_catalog_api_sale_location = cls(
            sale_location_type=sale_location_type,
            sale_location_type_id=sale_location_type_id,
            universe_ids=universe_ids,
            enabled_universe_ids=enabled_universe_ids,
        )

        return roblox_catalog_api_sale_location
