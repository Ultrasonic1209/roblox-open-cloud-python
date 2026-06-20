from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_localization_client_supported_locale_locale import RobloxLocalizationClientSupportedLocaleLocale
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_client_language_family import RobloxLocalizationClientLanguageFamily


T = TypeVar("T", bound="RobloxLocalizationClientSupportedLocale")


@_attrs_define
class RobloxLocalizationClientSupportedLocale:
    """
    Attributes:
        id (int | Unset):
        locale (RobloxLocalizationClientSupportedLocaleLocale | Unset):
        locale_code (str | Unset):
        name (str | Unset):
        native_name (str | Unset):
        language (RobloxLocalizationClientLanguageFamily | Unset):
    """

    id: int | Unset = UNSET
    locale: RobloxLocalizationClientSupportedLocaleLocale | Unset = UNSET
    locale_code: str | Unset = UNSET
    name: str | Unset = UNSET
    native_name: str | Unset = UNSET
    language: RobloxLocalizationClientLanguageFamily | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value

        locale_code = self.locale_code

        name = self.name

        native_name = self.native_name

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if locale_code is not UNSET:
            field_dict["localeCode"] = locale_code
        if name is not UNSET:
            field_dict["name"] = name
        if native_name is not UNSET:
            field_dict["nativeName"] = native_name
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_client_language_family import RobloxLocalizationClientLanguageFamily

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        _locale = d.pop("locale", UNSET)
        locale: RobloxLocalizationClientSupportedLocaleLocale | Unset
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = RobloxLocalizationClientSupportedLocaleLocale(_locale)

        locale_code = d.pop("localeCode", UNSET)

        name = d.pop("name", UNSET)

        native_name = d.pop("nativeName", UNSET)

        _language = d.pop("language", UNSET)
        language: RobloxLocalizationClientLanguageFamily | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = RobloxLocalizationClientLanguageFamily.from_dict(_language)

        roblox_localization_client_supported_locale = cls(
            id=id,
            locale=locale,
            locale_code=locale_code,
            name=name,
            native_name=native_name,
            language=language,
        )

        return roblox_localization_client_supported_locale
