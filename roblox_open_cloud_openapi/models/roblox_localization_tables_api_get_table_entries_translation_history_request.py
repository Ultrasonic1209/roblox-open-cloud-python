from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_cursor_entry_identifier import (
        RobloxLocalizationTablesApiCursorEntryIdentifier,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest")


@_attrs_define
class RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest:
    """
    Attributes:
        locale (str | Unset):
        entries (list[RobloxLocalizationTablesApiCursorEntryIdentifier] | Unset):
    """

    locale: str | Unset = UNSET
    entries: list[RobloxLocalizationTablesApiCursorEntryIdentifier] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_cursor_entry_identifier import (
            RobloxLocalizationTablesApiCursorEntryIdentifier,
        )

        d = dict(src_dict)
        locale = d.pop("locale", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[RobloxLocalizationTablesApiCursorEntryIdentifier] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = RobloxLocalizationTablesApiCursorEntryIdentifier.from_dict(entries_item_data)

                entries.append(entries_item)

        roblox_localization_tables_api_get_table_entries_translation_history_request = cls(
            locale=locale,
            entries=entries,
        )

        return roblox_localization_tables_api_get_table_entries_translation_history_request
