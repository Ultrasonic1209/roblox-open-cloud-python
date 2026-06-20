from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_internationalization_api_translation_count_translation_status import (
    RobloxGameInternationalizationApiTranslationCountTranslationStatus,
)
from ..models.roblox_game_internationalization_api_translation_count_translator_type import (
    RobloxGameInternationalizationApiTranslationCountTranslatorType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiTranslationCount")


@_attrs_define
class RobloxGameInternationalizationApiTranslationCount:
    """A model that contains the count value of a translation count and relevant metadata.

    Attributes:
        count (int | Unset):
        translation_status (RobloxGameInternationalizationApiTranslationCountTranslationStatus | Unset): The enum
            representing a translation status. ['Approved' = 0]
        translator_type (RobloxGameInternationalizationApiTranslationCountTranslatorType | Unset): Gets or sets the type
            of the translator associated with the count, or `null` if the count is not associated with a specific type of
            translator.
    """

    count: int | Unset = UNSET
    translation_status: RobloxGameInternationalizationApiTranslationCountTranslationStatus | Unset = UNSET
    translator_type: RobloxGameInternationalizationApiTranslationCountTranslatorType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        translation_status: str | Unset = UNSET
        if not isinstance(self.translation_status, Unset):
            translation_status = self.translation_status.value

        translator_type: str | Unset = UNSET
        if not isinstance(self.translator_type, Unset):
            translator_type = self.translator_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if translation_status is not UNSET:
            field_dict["translationStatus"] = translation_status
        if translator_type is not UNSET:
            field_dict["translatorType"] = translator_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        count = d.pop("count", UNSET)

        _translation_status = d.pop("translationStatus", UNSET)
        translation_status: RobloxGameInternationalizationApiTranslationCountTranslationStatus | Unset
        if isinstance(_translation_status, Unset):
            translation_status = UNSET
        else:
            translation_status = RobloxGameInternationalizationApiTranslationCountTranslationStatus(_translation_status)

        _translator_type = d.pop("translatorType", UNSET)
        translator_type: RobloxGameInternationalizationApiTranslationCountTranslatorType | Unset
        if isinstance(_translator_type, Unset):
            translator_type = UNSET
        else:
            translator_type = RobloxGameInternationalizationApiTranslationCountTranslatorType(_translator_type)

        roblox_game_internationalization_api_translation_count = cls(
            count=count,
            translation_status=translation_status,
            translator_type=translator_type,
        )

        return roblox_game_internationalization_api_translation_count
