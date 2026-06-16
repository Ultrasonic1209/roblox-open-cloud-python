from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_locale_api_supported_locale import RobloxLocaleApiSupportedLocale


T = TypeVar("T", bound="RobloxLocaleApiSupportedLocalesResponse")


@_attrs_define
class RobloxLocaleApiSupportedLocalesResponse:
    """Returns list of supported locales

    Attributes:
        supported_locales (list[RobloxLocaleApiSupportedLocale] | Unset): List of supported locales. Will be empty on
            error.
    """

    supported_locales: list[RobloxLocaleApiSupportedLocale] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        supported_locales: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.supported_locales, Unset):
            supported_locales = []
            for supported_locales_item_data in self.supported_locales:
                supported_locales_item = supported_locales_item_data.to_dict()
                supported_locales.append(supported_locales_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if supported_locales is not UNSET:
            field_dict["supportedLocales"] = supported_locales

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_locale_api_supported_locale import RobloxLocaleApiSupportedLocale

        d = dict(src_dict)
        _supported_locales = d.pop("supportedLocales", UNSET)
        supported_locales: list[RobloxLocaleApiSupportedLocale] | Unset = UNSET
        if _supported_locales is not UNSET:
            supported_locales = []
            for supported_locales_item_data in _supported_locales:
                supported_locales_item = RobloxLocaleApiSupportedLocale.from_dict(supported_locales_item_data)

                supported_locales.append(supported_locales_item)

        roblox_locale_api_supported_locales_response = cls(
            supported_locales=supported_locales,
        )

        return roblox_locale_api_supported_locales_response
