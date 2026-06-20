from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_locale_api_language import RobloxLocaleApiLanguage


T = TypeVar("T", bound="RobloxLocaleApiSupportedLocale")


@_attrs_define
class RobloxLocaleApiSupportedLocale:
    """Model for Supported locale

    Attributes:
        id (int | Unset): id of supported locale
        locale (str | Unset): locale of supported locale. Example "en-us"
        name (str | Unset): Name of supported locale.
        native_name (str | Unset): Name of supported locale in native language. Example "English"
        language (RobloxLocaleApiLanguage | Unset): Model for Language
    """

    id: int | Unset = UNSET
    locale: str | Unset = UNSET
    name: str | Unset = UNSET
    native_name: str | Unset = UNSET
    language: RobloxLocaleApiLanguage | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        locale = self.locale

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
        if name is not UNSET:
            field_dict["name"] = name
        if native_name is not UNSET:
            field_dict["nativeName"] = native_name
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_locale_api_language import RobloxLocaleApiLanguage

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        locale = d.pop("locale", UNSET)

        name = d.pop("name", UNSET)

        native_name = d.pop("nativeName", UNSET)

        _language = d.pop("language", UNSET)
        language: RobloxLocaleApiLanguage | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = RobloxLocaleApiLanguage.from_dict(_language)

        roblox_locale_api_supported_locale = cls(
            id=id,
            locale=locale,
            name=name,
            native_name=native_name,
            language=language,
        )

        return roblox_locale_api_supported_locale
