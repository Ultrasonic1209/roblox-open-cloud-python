from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_translation_history_paged import (
        RobloxLocalizationTablesApiEntryTranslationHistoryPaged,
    )
    from ..models.roblox_localization_tables_api_failed_entry_translation_history_paged import (
        RobloxLocalizationTablesApiFailedEntryTranslationHistoryPaged,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse")


@_attrs_define
class RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse:
    """A response model for GetTableEntriesTranslationHistory.

    Attributes:
        table_id (UUID | Unset): The entries' tableId.
        locale (str | Unset): The locale of the translations.
        entries (list[RobloxLocalizationTablesApiEntryTranslationHistoryPaged] | Unset): The entries with their
            identifier, translation history, and next cursor.
        failed_entries (list[RobloxLocalizationTablesApiFailedEntryTranslationHistoryPaged] | Unset): The failed
            entries.
    """

    table_id: UUID | Unset = UNSET
    locale: str | Unset = UNSET
    entries: list[RobloxLocalizationTablesApiEntryTranslationHistoryPaged] | Unset = UNSET
    failed_entries: list[RobloxLocalizationTablesApiFailedEntryTranslationHistoryPaged] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        table_id: str | Unset = UNSET
        if not isinstance(self.table_id, Unset):
            table_id = str(self.table_id)

        locale = self.locale

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        failed_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_entries, Unset):
            failed_entries = []
            for failed_entries_item_data in self.failed_entries:
                failed_entries_item = failed_entries_item_data.to_dict()
                failed_entries.append(failed_entries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if table_id is not UNSET:
            field_dict["tableId"] = table_id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if entries is not UNSET:
            field_dict["entries"] = entries
        if failed_entries is not UNSET:
            field_dict["failedEntries"] = failed_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_translation_history_paged import (
            RobloxLocalizationTablesApiEntryTranslationHistoryPaged,
        )
        from ..models.roblox_localization_tables_api_failed_entry_translation_history_paged import (
            RobloxLocalizationTablesApiFailedEntryTranslationHistoryPaged,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _table_id = d.pop("tableId", UNSET)
        table_id: UUID | Unset
        if isinstance(_table_id, Unset):
            table_id = UNSET
        else:
            table_id = UUID(_table_id)

        locale = d.pop("locale", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[RobloxLocalizationTablesApiEntryTranslationHistoryPaged] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = RobloxLocalizationTablesApiEntryTranslationHistoryPaged.from_dict(entries_item_data)

                entries.append(entries_item)

        _failed_entries = d.pop("failedEntries", UNSET)
        failed_entries: list[RobloxLocalizationTablesApiFailedEntryTranslationHistoryPaged] | Unset = UNSET
        if _failed_entries is not UNSET:
            failed_entries = []
            for failed_entries_item_data in _failed_entries:
                failed_entries_item = RobloxLocalizationTablesApiFailedEntryTranslationHistoryPaged.from_dict(
                    failed_entries_item_data
                )

                failed_entries.append(failed_entries_item)

        roblox_localization_tables_api_get_table_entries_translation_history_response = cls(
            table_id=table_id,
            locale=locale,
            entries=entries,
            failed_entries=failed_entries,
        )

        return roblox_localization_tables_api_get_table_entries_translation_history_response
