from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_translator import RobloxGameInternationalizationApiTranslator


T = TypeVar("T", bound="RobloxGameInternationalizationApiTranslationHistory")


@_attrs_define
class RobloxGameInternationalizationApiTranslationHistory:
    """A model containing a translation, translator, and translation time.

    Attributes:
        translation_text (str | Unset): The translation provided by the translator.
        translator (RobloxGameInternationalizationApiTranslator | Unset):
        created (datetime.datetime | Unset): The time the translation was provided.
    """

    translation_text: str | Unset = UNSET
    translator: RobloxGameInternationalizationApiTranslator | Unset = UNSET
    created: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        translation_text = self.translation_text

        translator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translator, Unset):
            translator = self.translator.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if translation_text is not UNSET:
            field_dict["translationText"] = translation_text
        if translator is not UNSET:
            field_dict["translator"] = translator
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_translator import RobloxGameInternationalizationApiTranslator

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        translation_text = d.pop("translationText", UNSET)

        _translator = d.pop("translator", UNSET)
        translator: RobloxGameInternationalizationApiTranslator | Unset
        if isinstance(_translator, Unset):
            translator = UNSET
        else:
            translator = RobloxGameInternationalizationApiTranslator.from_dict(_translator)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        roblox_game_internationalization_api_translation_history = cls(
            translation_text=translation_text,
            translator=translator,
            created=created,
        )

        return roblox_game_internationalization_api_translation_history
