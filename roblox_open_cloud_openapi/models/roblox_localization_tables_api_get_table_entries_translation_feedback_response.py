from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_translation_feedback import (
        RobloxLocalizationTablesApiEntryTranslationFeedback,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiGetTableEntriesTranslationFeedbackResponse")


@_attrs_define
class RobloxLocalizationTablesApiGetTableEntriesTranslationFeedbackResponse:
    """A response model for GetTableEntriesTranslationFeedback.

    Attributes:
        table_id (UUID | Unset): The entries' tableId.
        entries (list[RobloxLocalizationTablesApiEntryTranslationFeedback] | Unset): The entries with their identifier,
            translation feedback details.
    """

    table_id: UUID | Unset = UNSET
    entries: list[RobloxLocalizationTablesApiEntryTranslationFeedback] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        table_id: str | Unset = UNSET
        if not isinstance(self.table_id, Unset):
            table_id = str(self.table_id)

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if table_id is not UNSET:
            field_dict["tableId"] = table_id
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_translation_feedback import (
            RobloxLocalizationTablesApiEntryTranslationFeedback,
        )

        d = dict(src_dict)
        _table_id = d.pop("tableId", UNSET)
        table_id: UUID | Unset
        if isinstance(_table_id, Unset):
            table_id = UNSET
        else:
            table_id = UUID(_table_id)

        _entries = d.pop("entries", UNSET)
        entries: list[RobloxLocalizationTablesApiEntryTranslationFeedback] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = RobloxLocalizationTablesApiEntryTranslationFeedback.from_dict(entries_item_data)

                entries.append(entries_item)

        roblox_localization_tables_api_get_table_entries_translation_feedback_response = cls(
            table_id=table_id,
            entries=entries,
        )

        return roblox_localization_tables_api_get_table_entries_translation_feedback_response
