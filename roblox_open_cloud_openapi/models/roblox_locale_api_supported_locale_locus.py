from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_locale_api_supported_locale import RobloxLocaleApiSupportedLocale


T = TypeVar("T", bound="RobloxLocaleApiSupportedLocaleLocus")


@_attrs_define
class RobloxLocaleApiSupportedLocaleLocus:
    """Model for Supported locale with user locus information

    Attributes:
        locale (RobloxLocaleApiSupportedLocale | Unset): Model for Supported locale
        is_enabled_for_full_experience (bool | Unset): Is locale enabled for full experience
        is_enabled_for_signup_and_login (bool | Unset): Is locale enabled for signup and login
        is_enabled_for_in_game_ugc (bool | Unset): Is locale enabled for in game ugc
    """

    locale: RobloxLocaleApiSupportedLocale | Unset = UNSET
    is_enabled_for_full_experience: bool | Unset = UNSET
    is_enabled_for_signup_and_login: bool | Unset = UNSET
    is_enabled_for_in_game_ugc: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        locale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.to_dict()

        is_enabled_for_full_experience = self.is_enabled_for_full_experience

        is_enabled_for_signup_and_login = self.is_enabled_for_signup_and_login

        is_enabled_for_in_game_ugc = self.is_enabled_for_in_game_ugc

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if is_enabled_for_full_experience is not UNSET:
            field_dict["isEnabledForFullExperience"] = is_enabled_for_full_experience
        if is_enabled_for_signup_and_login is not UNSET:
            field_dict["isEnabledForSignupAndLogin"] = is_enabled_for_signup_and_login
        if is_enabled_for_in_game_ugc is not UNSET:
            field_dict["isEnabledForInGameUgc"] = is_enabled_for_in_game_ugc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_locale_api_supported_locale import RobloxLocaleApiSupportedLocale

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _locale = d.pop("locale", UNSET)
        locale: RobloxLocaleApiSupportedLocale | Unset
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = RobloxLocaleApiSupportedLocale.from_dict(_locale)

        is_enabled_for_full_experience = d.pop("isEnabledForFullExperience", UNSET)

        is_enabled_for_signup_and_login = d.pop("isEnabledForSignupAndLogin", UNSET)

        is_enabled_for_in_game_ugc = d.pop("isEnabledForInGameUgc", UNSET)

        roblox_locale_api_supported_locale_locus = cls(
            locale=locale,
            is_enabled_for_full_experience=is_enabled_for_full_experience,
            is_enabled_for_signup_and_login=is_enabled_for_signup_and_login,
            is_enabled_for_in_game_ugc=is_enabled_for_in_game_ugc,
        )

        return roblox_locale_api_supported_locale_locus
