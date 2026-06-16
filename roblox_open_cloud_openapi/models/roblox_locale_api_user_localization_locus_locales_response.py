from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_locale_api_supported_locale import RobloxLocaleApiSupportedLocale


T = TypeVar("T", bound="RobloxLocaleApiUserLocalizationLocusLocalesResponse")


@_attrs_define
class RobloxLocaleApiUserLocalizationLocusLocalesResponse:
    """Returns available Roblox.Locale.Api.SupportedLocale models.

    Attributes:
        signup_and_login (RobloxLocaleApiSupportedLocale | Unset): Model for Supported locale
        general_experience (RobloxLocaleApiSupportedLocale | Unset): Model for Supported locale
        ugc (RobloxLocaleApiSupportedLocale | Unset): Model for Supported locale
        show_roblox_translations (bool | Unset): Whether Roblox-suggested translations should be shown to the user.
    """

    signup_and_login: RobloxLocaleApiSupportedLocale | Unset = UNSET
    general_experience: RobloxLocaleApiSupportedLocale | Unset = UNSET
    ugc: RobloxLocaleApiSupportedLocale | Unset = UNSET
    show_roblox_translations: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        signup_and_login: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signup_and_login, Unset):
            signup_and_login = self.signup_and_login.to_dict()

        general_experience: dict[str, Any] | Unset = UNSET
        if not isinstance(self.general_experience, Unset):
            general_experience = self.general_experience.to_dict()

        ugc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ugc, Unset):
            ugc = self.ugc.to_dict()

        show_roblox_translations = self.show_roblox_translations

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if signup_and_login is not UNSET:
            field_dict["signupAndLogin"] = signup_and_login
        if general_experience is not UNSET:
            field_dict["generalExperience"] = general_experience
        if ugc is not UNSET:
            field_dict["ugc"] = ugc
        if show_roblox_translations is not UNSET:
            field_dict["showRobloxTranslations"] = show_roblox_translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_locale_api_supported_locale import RobloxLocaleApiSupportedLocale

        d = dict(src_dict)
        _signup_and_login = d.pop("signupAndLogin", UNSET)
        signup_and_login: RobloxLocaleApiSupportedLocale | Unset
        if isinstance(_signup_and_login, Unset):
            signup_and_login = UNSET
        else:
            signup_and_login = RobloxLocaleApiSupportedLocale.from_dict(_signup_and_login)

        _general_experience = d.pop("generalExperience", UNSET)
        general_experience: RobloxLocaleApiSupportedLocale | Unset
        if isinstance(_general_experience, Unset):
            general_experience = UNSET
        else:
            general_experience = RobloxLocaleApiSupportedLocale.from_dict(_general_experience)

        _ugc = d.pop("ugc", UNSET)
        ugc: RobloxLocaleApiSupportedLocale | Unset
        if isinstance(_ugc, Unset):
            ugc = UNSET
        else:
            ugc = RobloxLocaleApiSupportedLocale.from_dict(_ugc)

        show_roblox_translations = d.pop("showRobloxTranslations", UNSET)

        roblox_locale_api_user_localization_locus_locales_response = cls(
            signup_and_login=signup_and_login,
            general_experience=general_experience,
            ugc=ugc,
            show_roblox_translations=show_roblox_translations,
        )

        return roblox_locale_api_user_localization_locus_locales_response
