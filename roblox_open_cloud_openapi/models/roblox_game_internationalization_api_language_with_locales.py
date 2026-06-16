from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_language import RobloxGameInternationalizationApiLanguage
    from ..models.roblox_localization_client_supported_locale import RobloxLocalizationClientSupportedLocale


T = TypeVar("T", bound="RobloxGameInternationalizationApiLanguageWithLocales")


@_attrs_define
class RobloxGameInternationalizationApiLanguageWithLocales:
    """
    Attributes:
        language_family (RobloxGameInternationalizationApiLanguage | Unset):
        child_locales (list[RobloxLocalizationClientSupportedLocale] | Unset):
    """

    language_family: RobloxGameInternationalizationApiLanguage | Unset = UNSET
    child_locales: list[RobloxLocalizationClientSupportedLocale] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        language_family: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language_family, Unset):
            language_family = self.language_family.to_dict()

        child_locales: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.child_locales, Unset):
            child_locales = []
            for child_locales_item_data in self.child_locales:
                child_locales_item = child_locales_item_data.to_dict()
                child_locales.append(child_locales_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if language_family is not UNSET:
            field_dict["languageFamily"] = language_family
        if child_locales is not UNSET:
            field_dict["childLocales"] = child_locales

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_language import RobloxGameInternationalizationApiLanguage
        from ..models.roblox_localization_client_supported_locale import RobloxLocalizationClientSupportedLocale

        d = dict(src_dict)
        _language_family = d.pop("languageFamily", UNSET)
        language_family: RobloxGameInternationalizationApiLanguage | Unset
        if isinstance(_language_family, Unset):
            language_family = UNSET
        else:
            language_family = RobloxGameInternationalizationApiLanguage.from_dict(_language_family)

        _child_locales = d.pop("childLocales", UNSET)
        child_locales: list[RobloxLocalizationClientSupportedLocale] | Unset = UNSET
        if _child_locales is not UNSET:
            child_locales = []
            for child_locales_item_data in _child_locales:
                child_locales_item = RobloxLocalizationClientSupportedLocale.from_dict(child_locales_item_data)

                child_locales.append(child_locales_item)

        roblox_game_internationalization_api_language_with_locales = cls(
            language_family=language_family,
            child_locales=child_locales,
        )

        return roblox_game_internationalization_api_language_with_locales
