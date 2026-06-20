from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_translator import RobloxLocalizationTablesApiTranslator


T = TypeVar("T", bound="RobloxLocalizationTablesApiTranslation")


@_attrs_define
class RobloxLocalizationTablesApiTranslation:
    """
    Attributes:
        locale (str | Unset):
        translation_text (str | Unset):
        translator (RobloxLocalizationTablesApiTranslator | Unset):
        updated_time (datetime.datetime | Unset):
        feedback_count (int | Unset):
    """

    locale: str | Unset = UNSET
    translation_text: str | Unset = UNSET
    translator: RobloxLocalizationTablesApiTranslator | Unset = UNSET
    updated_time: datetime.datetime | Unset = UNSET
    feedback_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        translation_text = self.translation_text

        translator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translator, Unset):
            translator = self.translator.to_dict()

        updated_time: str | Unset = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        feedback_count = self.feedback_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if translation_text is not UNSET:
            field_dict["translationText"] = translation_text
        if translator is not UNSET:
            field_dict["translator"] = translator
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time
        if feedback_count is not UNSET:
            field_dict["feedbackCount"] = feedback_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_translator import RobloxLocalizationTablesApiTranslator

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        locale = d.pop("locale", UNSET)

        translation_text = d.pop("translationText", UNSET)

        _translator = d.pop("translator", UNSET)
        translator: RobloxLocalizationTablesApiTranslator | Unset
        if isinstance(_translator, Unset):
            translator = UNSET
        else:
            translator = RobloxLocalizationTablesApiTranslator.from_dict(_translator)

        _updated_time = d.pop("updatedTime", UNSET)
        updated_time: datetime.datetime | Unset
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = datetime.datetime.fromisoformat(_updated_time)

        feedback_count = d.pop("feedbackCount", UNSET)

        roblox_localization_tables_api_translation = cls(
            locale=locale,
            translation_text=translation_text,
            translator=translator,
            updated_time=updated_time,
            feedback_count=feedback_count,
        )

        return roblox_localization_tables_api_translation
