from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_translation_count_game_info_response_status import (
    RobloxGameInternationalizationApiTranslationCountGameInfoResponseStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_translation_count_category_info_response import (
        RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiTranslationCountGameInfoResponse")


@_attrs_define
class RobloxGameInternationalizationApiTranslationCountGameInfoResponse:
    """A response model that contains game info for getting a translation count.

    Attributes:
        game_id (int | Unset): The game id.
        status (RobloxGameInternationalizationApiTranslationCountGameInfoResponseStatus | Unset): The status of the
            response for the requested game. ['LanguageOrLocaleSupportedForGame' = 0, 'LanguageOrLocaleNotSupportedForGame'
            = 1, 'LanguageOrLocaleIsSource' = 2, 'InsufficientPermission' = 3, 'GameDoesNotExist' = 4,
            'GameDoesNotHaveTable' = 5, 'UnknownError' = 6]
        categories (list[RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse] | Unset): Categories of
            translation counts.
    """

    game_id: int | Unset = UNSET
    status: RobloxGameInternationalizationApiTranslationCountGameInfoResponseStatus | Unset = UNSET
    categories: list[RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        game_id = self.game_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if game_id is not UNSET:
            field_dict["gameId"] = game_id
        if status is not UNSET:
            field_dict["status"] = status
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_translation_count_category_info_response import (
            RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        game_id = d.pop("gameId", UNSET)

        _status = d.pop("status", UNSET)
        status: RobloxGameInternationalizationApiTranslationCountGameInfoResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RobloxGameInternationalizationApiTranslationCountGameInfoResponseStatus(_status)

        _categories = d.pop("categories", UNSET)
        categories: list[RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = RobloxGameInternationalizationApiTranslationCountCategoryInfoResponse.from_dict(
                    categories_item_data
                )

                categories.append(categories_item)

        roblox_game_internationalization_api_translation_count_game_info_response = cls(
            game_id=game_id,
            status=status,
            categories=categories,
        )

        return roblox_game_internationalization_api_translation_count_game_info_response
