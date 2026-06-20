from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_translation_count_language_or_locale_response_language_code_type import (
    RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseLanguageCodeType,
)
from ..models.roblox_game_internationalization_api_translation_count_language_or_locale_response_status import (
    RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_translation_count_category_info_response import (
        RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponse")


@_attrs_define
class RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponse:
    """
    Attributes:
        status (RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseStatus | Unset): The status of
            the response for the requested game. ['Success' = 1, 'LanguageOrLocaleNotSupportedForGame' = 2]
        categories (list[RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse] | Unset): Categories of
            translation counts.
        name (str | Unset):
        language_code_type (RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseLanguageCodeType |
            Unset): An enum to distinguish between locale codes and language codes. ['Language' = 0, 'Locale' = 1]
        language_code (str | Unset):
    """

    status: RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseStatus | Unset = UNSET
    categories: list[RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse] | Unset = UNSET
    name: str | Unset = UNSET
    language_code_type: (
        RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseLanguageCodeType | Unset
    ) = UNSET
    language_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        name = self.name

        language_code_type: str | Unset = UNSET
        if not isinstance(self.language_code_type, Unset):
            language_code_type = self.language_code_type.value

        language_code = self.language_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if categories is not UNSET:
            field_dict["categories"] = categories
        if name is not UNSET:
            field_dict["name"] = name
        if language_code_type is not UNSET:
            field_dict["languageCodeType"] = language_code_type
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_translation_count_category_info_response import (
            RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _status = d.pop("status", UNSET)
        status: RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseStatus(_status)

        _categories = d.pop("categories", UNSET)
        categories: list[RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse.from_dict(
                    categories_item_data
                )

                categories.append(categories_item)

        name = d.pop("name", UNSET)

        _language_code_type = d.pop("languageCodeType", UNSET)
        language_code_type: (
            RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseLanguageCodeType | Unset
        )
        if isinstance(_language_code_type, Unset):
            language_code_type = UNSET
        else:
            language_code_type = (
                RobloxGameInternationalizationApiTranslationCountLanguageOrLocaleResponseLanguageCodeType(
                    _language_code_type
                )
            )

        language_code = d.pop("languageCode", UNSET)

        roblox_game_internationalization_api_translation_count_language_or_locale_response = cls(
            status=status,
            categories=categories,
            name=name,
            language_code_type=language_code_type,
            language_code=language_code,
        )

        return roblox_game_internationalization_api_translation_count_language_or_locale_response
