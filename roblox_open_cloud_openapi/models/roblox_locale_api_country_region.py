from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocaleApiCountryRegion")


@_attrs_define
class RobloxLocaleApiCountryRegion:
    """Model for Country Regions

    Attributes:
        code (str | Unset): code of country region
        name (str | Unset): native name of country region
        display_name (str | Unset): localized name of country region. Example "Afghanistan"
    """

    code: str | Unset = UNSET
    name: str | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        roblox_locale_api_country_region = cls(
            code=code,
            name=name,
            display_name=display_name,
        )

        return roblox_locale_api_country_region
