from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiGetRepresentativeCountriesResponse")


@_attrs_define
class RobloxItemConfigurationApiGetRepresentativeCountriesResponse:
    """Defines the response model for the GET v1/collectibles/regional-pricing/representative-countries.

    Attributes:
        country_iso_2_codes (list[str] | Unset): List of representative countries.
    """

    country_iso_2_codes: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country_iso_2_codes: list[str] | Unset = UNSET
        if not isinstance(self.country_iso_2_codes, Unset):
            country_iso_2_codes = self.country_iso_2_codes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country_iso_2_codes is not UNSET:
            field_dict["countryIso2Codes"] = country_iso_2_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_iso_2_codes = cast(list[str], d.pop("countryIso2Codes", UNSET))

        roblox_item_configuration_api_get_representative_countries_response = cls(
            country_iso_2_codes=country_iso_2_codes,
        )

        return roblox_item_configuration_api_get_representative_countries_response
