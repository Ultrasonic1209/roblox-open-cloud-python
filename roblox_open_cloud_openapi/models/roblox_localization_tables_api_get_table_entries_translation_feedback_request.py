from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_identifier_with_translation import (
        RobloxLocalizationTablesApiEntryIdentifierWithTranslation,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiGetTableEntriesTranslationFeedbackRequest")


@_attrs_define
class RobloxLocalizationTablesApiGetTableEntriesTranslationFeedbackRequest:
    """A request model for GetTableEntriesTranslationFeedback.

    Attributes:
        source_locale (str | Unset): locale code of source language, we only accept language code at the moment.
        entries (list[RobloxLocalizationTablesApiEntryIdentifierWithTranslation] | Unset): entry identifier
    """

    source_locale: str | Unset = UNSET
    entries: list[RobloxLocalizationTablesApiEntryIdentifierWithTranslation] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_locale = self.source_locale

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if source_locale is not UNSET:
            field_dict["sourceLocale"] = source_locale
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_identifier_with_translation import (
            RobloxLocalizationTablesApiEntryIdentifierWithTranslation,
        )

        d = dict(src_dict)
        source_locale = d.pop("sourceLocale", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[RobloxLocalizationTablesApiEntryIdentifierWithTranslation] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = RobloxLocalizationTablesApiEntryIdentifierWithTranslation.from_dict(entries_item_data)

                entries.append(entries_item)

        roblox_localization_tables_api_get_table_entries_translation_feedback_request = cls(
            source_locale=source_locale,
            entries=entries,
        )

        return roblox_localization_tables_api_get_table_entries_translation_feedback_request
