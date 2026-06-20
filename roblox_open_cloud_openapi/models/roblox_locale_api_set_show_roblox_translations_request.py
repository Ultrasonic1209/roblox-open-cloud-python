from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocaleApiSetShowRobloxTranslationsRequest")


@_attrs_define
class RobloxLocaleApiSetShowRobloxTranslationsRequest:
    """Request entity to set the ShowRobloxTranslations field for an account

    Attributes:
        show_roblox_translations (bool | Unset): Value to set the ShowRobloxTranslations field to
    """

    show_roblox_translations: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        show_roblox_translations = self.show_roblox_translations

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if show_roblox_translations is not UNSET:
            field_dict["showRobloxTranslations"] = show_roblox_translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        show_roblox_translations = d.pop("showRobloxTranslations", UNSET)

        roblox_locale_api_set_show_roblox_translations_request = cls(
            show_roblox_translations=show_roblox_translations,
        )

        return roblox_locale_api_set_show_roblox_translations_request
