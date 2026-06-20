from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_localization_tables_api_entry_identifier_with_translation_entry_format import (
    RobloxLocalizationTablesApiEntryIdentifierWithTranslationEntryFormat,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_translation import RobloxLocalizationTablesApiTranslation


T = TypeVar("T", bound="RobloxLocalizationTablesApiEntryIdentifierWithTranslation")


@_attrs_define
class RobloxLocalizationTablesApiEntryIdentifierWithTranslation:
    """
    Attributes:
        translation (RobloxLocalizationTablesApiTranslation | Unset):
        key (str | Unset):
        context (str | Unset):
        source (str | Unset):
        entry_format (RobloxLocalizationTablesApiEntryIdentifierWithTranslationEntryFormat | Unset):
    """

    translation: RobloxLocalizationTablesApiTranslation | Unset = UNSET
    key: str | Unset = UNSET
    context: str | Unset = UNSET
    source: str | Unset = UNSET
    entry_format: RobloxLocalizationTablesApiEntryIdentifierWithTranslationEntryFormat | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        translation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translation, Unset):
            translation = self.translation.to_dict()

        key = self.key

        context = self.context

        source = self.source

        entry_format: str | Unset = UNSET
        if not isinstance(self.entry_format, Unset):
            entry_format = self.entry_format.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if translation is not UNSET:
            field_dict["translation"] = translation
        if key is not UNSET:
            field_dict["key"] = key
        if context is not UNSET:
            field_dict["context"] = context
        if source is not UNSET:
            field_dict["source"] = source
        if entry_format is not UNSET:
            field_dict["entryFormat"] = entry_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_translation import RobloxLocalizationTablesApiTranslation

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _translation = d.pop("translation", UNSET)
        translation: RobloxLocalizationTablesApiTranslation | Unset
        if isinstance(_translation, Unset):
            translation = UNSET
        else:
            translation = RobloxLocalizationTablesApiTranslation.from_dict(_translation)

        key = d.pop("key", UNSET)

        context = d.pop("context", UNSET)

        source = d.pop("source", UNSET)

        _entry_format = d.pop("entryFormat", UNSET)
        entry_format: RobloxLocalizationTablesApiEntryIdentifierWithTranslationEntryFormat | Unset
        if isinstance(_entry_format, Unset):
            entry_format = UNSET
        else:
            entry_format = RobloxLocalizationTablesApiEntryIdentifierWithTranslationEntryFormat(_entry_format)

        roblox_localization_tables_api_entry_identifier_with_translation = cls(
            translation=translation,
            key=key,
            context=context,
            source=source,
            entry_format=entry_format,
        )

        return roblox_localization_tables_api_entry_identifier_with_translation
