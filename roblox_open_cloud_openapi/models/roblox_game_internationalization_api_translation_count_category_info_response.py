from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_translation_count_category_info_response_category import (
    RobloxGameInternationalizationApiTranslationCountCategoryInfoResponseCategory,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_translation_count import (
        RobloxGameInternationalizationApiTranslationCount,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse")


@_attrs_define
class RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse:
    """A response model that contains category info for getting a translation count.

    Attributes:
        category (RobloxGameInternationalizationApiTranslationCountCategoryInfoResponseCategory | Unset): The category
            of the translation counts. ['InGameContent' = 0]
        translation_counts (list[RobloxGameInternationalizationApiTranslationCount] | Unset): The translation counts.
        total_translatable_item_count (int | Unset): The total number of translatable items.
            The translation count percentage can be calculated by doing translationCounts / totalTranslatableItemCount.
    """

    category: RobloxGameInternationalizationApiTranslationCountCategoryInfoResponseCategory | Unset = UNSET
    translation_counts: list[RobloxGameInternationalizationApiTranslationCount] | Unset = UNSET
    total_translatable_item_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        translation_counts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.translation_counts, Unset):
            translation_counts = []
            for translation_counts_item_data in self.translation_counts:
                translation_counts_item = translation_counts_item_data.to_dict()
                translation_counts.append(translation_counts_item)

        total_translatable_item_count = self.total_translatable_item_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if translation_counts is not UNSET:
            field_dict["translationCounts"] = translation_counts
        if total_translatable_item_count is not UNSET:
            field_dict["totalTranslatableItemCount"] = total_translatable_item_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_translation_count import (
            RobloxGameInternationalizationApiTranslationCount,
        )

        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: RobloxGameInternationalizationApiTranslationCountCategoryInfoResponseCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = RobloxGameInternationalizationApiTranslationCountCategoryInfoResponseCategory(_category)

        _translation_counts = d.pop("translationCounts", UNSET)
        translation_counts: list[RobloxGameInternationalizationApiTranslationCount] | Unset = UNSET
        if _translation_counts is not UNSET:
            translation_counts = []
            for translation_counts_item_data in _translation_counts:
                translation_counts_item = RobloxGameInternationalizationApiTranslationCount.from_dict(
                    translation_counts_item_data
                )

                translation_counts.append(translation_counts_item)

        total_translatable_item_count = d.pop("totalTranslatableItemCount", UNSET)

        roblox_game_internationalization_api_translation_count_category_info_response = cls(
            category=category,
            translation_counts=translation_counts,
            total_translatable_item_count=total_translatable_item_count,
        )

        return roblox_game_internationalization_api_translation_count_category_info_response
