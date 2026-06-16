from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiModelsResponseUserAccountCountry")


@_attrs_define
class RobloxAccountSettingsApiModelsResponseUserAccountCountry:
    """
    Attributes:
        country_name (str | Unset):
        subdivision_iso (str | Unset):
        localized_subdivision (str | Unset):
        localized_name (str | Unset):
        country_id (int | Unset):
    """

    country_name: str | Unset = UNSET
    subdivision_iso: str | Unset = UNSET
    localized_subdivision: str | Unset = UNSET
    localized_name: str | Unset = UNSET
    country_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country_name = self.country_name

        subdivision_iso = self.subdivision_iso

        localized_subdivision = self.localized_subdivision

        localized_name = self.localized_name

        country_id = self.country_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country_name is not UNSET:
            field_dict["countryName"] = country_name
        if subdivision_iso is not UNSET:
            field_dict["subdivisionIso"] = subdivision_iso
        if localized_subdivision is not UNSET:
            field_dict["localizedSubdivision"] = localized_subdivision
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if country_id is not UNSET:
            field_dict["countryId"] = country_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_name = d.pop("countryName", UNSET)

        subdivision_iso = d.pop("subdivisionIso", UNSET)

        localized_subdivision = d.pop("localizedSubdivision", UNSET)

        localized_name = d.pop("localizedName", UNSET)

        country_id = d.pop("countryId", UNSET)

        roblox_account_settings_api_models_response_user_account_country = cls(
            country_name=country_name,
            subdivision_iso=subdivision_iso,
            localized_subdivision=localized_subdivision,
            localized_name=localized_name,
            country_id=country_id,
        )

        return roblox_account_settings_api_models_response_user_account_country
