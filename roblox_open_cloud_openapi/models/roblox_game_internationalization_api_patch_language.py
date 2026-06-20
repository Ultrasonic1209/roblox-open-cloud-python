from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_patch_language_language_code_type import (
    RobloxGameInternationalizationApiPatchLanguageLanguageCodeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiPatchLanguage")


@_attrs_define
class RobloxGameInternationalizationApiPatchLanguage:
    """
    Attributes:
        language_code_type (RobloxGameInternationalizationApiPatchLanguageLanguageCodeType | Unset): The language code
            type. ['Language' = 0, 'Locale' = 1]
        language_code (str | Unset): The language code for the language to edit.
        delete (bool | Unset): An optional field used to indicate whether a language should be deleted from this game's
            list of supported languages.
    """

    language_code_type: RobloxGameInternationalizationApiPatchLanguageLanguageCodeType | Unset = UNSET
    language_code: str | Unset = UNSET
    delete: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        language_code_type: str | Unset = UNSET
        if not isinstance(self.language_code_type, Unset):
            language_code_type = self.language_code_type.value

        language_code = self.language_code

        delete = self.delete

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if language_code_type is not UNSET:
            field_dict["languageCodeType"] = language_code_type
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _language_code_type = d.pop("languageCodeType", UNSET)
        language_code_type: RobloxGameInternationalizationApiPatchLanguageLanguageCodeType | Unset
        if isinstance(_language_code_type, Unset):
            language_code_type = UNSET
        else:
            language_code_type = RobloxGameInternationalizationApiPatchLanguageLanguageCodeType(_language_code_type)

        language_code = d.pop("languageCode", UNSET)

        delete = d.pop("delete", UNSET)

        roblox_game_internationalization_api_patch_language = cls(
            language_code_type=language_code_type,
            language_code=language_code,
            delete=delete,
        )

        return roblox_game_internationalization_api_patch_language
