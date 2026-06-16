from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_locale_api_country_region import RobloxLocaleApiCountryRegion


T = TypeVar("T", bound="RobloxLocaleApiCountryRegionListResponse")


@_attrs_define
class RobloxLocaleApiCountryRegionListResponse:
    """Returns list of supported country/regions

    Attributes:
        country_region_list (list[RobloxLocaleApiCountryRegion] | Unset): List of supported country/regions. Will be
            empty on error.
    """

    country_region_list: list[RobloxLocaleApiCountryRegion] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country_region_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.country_region_list, Unset):
            country_region_list = []
            for country_region_list_item_data in self.country_region_list:
                country_region_list_item = country_region_list_item_data.to_dict()
                country_region_list.append(country_region_list_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country_region_list is not UNSET:
            field_dict["countryRegionList"] = country_region_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_locale_api_country_region import RobloxLocaleApiCountryRegion

        d = dict(src_dict)
        _country_region_list = d.pop("countryRegionList", UNSET)
        country_region_list: list[RobloxLocaleApiCountryRegion] | Unset = UNSET
        if _country_region_list is not UNSET:
            country_region_list = []
            for country_region_list_item_data in _country_region_list:
                country_region_list_item = RobloxLocaleApiCountryRegion.from_dict(country_region_list_item_data)

                country_region_list.append(country_region_list_item)

        roblox_locale_api_country_region_list_response = cls(
            country_region_list=country_region_list,
        )

        return roblox_locale_api_country_region_list_response
