from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_locale_api_language import RobloxLocaleApiLanguage
    from ..models.roblox_locale_api_supported_locale import RobloxLocaleApiSupportedLocale


T = TypeVar("T", bound="RobloxLocaleApiUserLocaleResponse")


@_attrs_define
class RobloxLocaleApiUserLocaleResponse:
    """
    Attributes:
        supported_locale (RobloxLocaleApiSupportedLocale | Unset): Model for Supported locale
        native_language (RobloxLocaleApiLanguage | Unset): Model for Language
    """

    supported_locale: RobloxLocaleApiSupportedLocale | Unset = UNSET
    native_language: RobloxLocaleApiLanguage | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        supported_locale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supported_locale, Unset):
            supported_locale = self.supported_locale.to_dict()

        native_language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.native_language, Unset):
            native_language = self.native_language.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if supported_locale is not UNSET:
            field_dict["supportedLocale"] = supported_locale
        if native_language is not UNSET:
            field_dict["nativeLanguage"] = native_language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_locale_api_language import RobloxLocaleApiLanguage
        from ..models.roblox_locale_api_supported_locale import RobloxLocaleApiSupportedLocale

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _supported_locale = d.pop("supportedLocale", UNSET)
        supported_locale: RobloxLocaleApiSupportedLocale | Unset
        if isinstance(_supported_locale, Unset):
            supported_locale = UNSET
        else:
            supported_locale = RobloxLocaleApiSupportedLocale.from_dict(_supported_locale)

        _native_language = d.pop("nativeLanguage", UNSET)
        native_language: RobloxLocaleApiLanguage | Unset
        if isinstance(_native_language, Unset):
            native_language = UNSET
        else:
            native_language = RobloxLocaleApiLanguage.from_dict(_native_language)

        roblox_locale_api_user_locale_response = cls(
            supported_locale=supported_locale,
            native_language=native_language,
        )

        return roblox_locale_api_user_locale_response
