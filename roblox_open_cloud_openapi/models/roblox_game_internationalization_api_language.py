from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiLanguage")


@_attrs_define
class RobloxGameInternationalizationApiLanguage:
    """
    Attributes:
        name (str | Unset):
        native_name (str | Unset):
        language_code (str | Unset):
    """

    name: str | Unset = UNSET
    native_name: str | Unset = UNSET
    language_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        native_name = self.native_name

        language_code = self.language_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if native_name is not UNSET:
            field_dict["nativeName"] = native_name
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        native_name = d.pop("nativeName", UNSET)

        language_code = d.pop("languageCode", UNSET)

        roblox_game_internationalization_api_language = cls(
            name=name,
            native_name=native_name,
            language_code=language_code,
        )

        return roblox_game_internationalization_api_language
