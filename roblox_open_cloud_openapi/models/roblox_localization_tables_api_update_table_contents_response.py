from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_failed_entry import RobloxLocalizationTablesApiFailedEntry
    from ..models.roblox_localization_tables_api_modified_entry import RobloxLocalizationTablesApiModifiedEntry


T = TypeVar("T", bound="RobloxLocalizationTablesApiUpdateTableContentsResponse")


@_attrs_define
class RobloxLocalizationTablesApiUpdateTableContentsResponse:
    """
    Attributes:
        failed_entries_and_translations (list[RobloxLocalizationTablesApiFailedEntry] | Unset):
        modified_entries_and_translations (list[RobloxLocalizationTablesApiModifiedEntry] | Unset):
    """

    failed_entries_and_translations: list[RobloxLocalizationTablesApiFailedEntry] | Unset = UNSET
    modified_entries_and_translations: list[RobloxLocalizationTablesApiModifiedEntry] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        failed_entries_and_translations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_entries_and_translations, Unset):
            failed_entries_and_translations = []
            for failed_entries_and_translations_item_data in self.failed_entries_and_translations:
                failed_entries_and_translations_item = failed_entries_and_translations_item_data.to_dict()
                failed_entries_and_translations.append(failed_entries_and_translations_item)

        modified_entries_and_translations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.modified_entries_and_translations, Unset):
            modified_entries_and_translations = []
            for modified_entries_and_translations_item_data in self.modified_entries_and_translations:
                modified_entries_and_translations_item = modified_entries_and_translations_item_data.to_dict()
                modified_entries_and_translations.append(modified_entries_and_translations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if failed_entries_and_translations is not UNSET:
            field_dict["failedEntriesAndTranslations"] = failed_entries_and_translations
        if modified_entries_and_translations is not UNSET:
            field_dict["modifiedEntriesAndTranslations"] = modified_entries_and_translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_failed_entry import RobloxLocalizationTablesApiFailedEntry
        from ..models.roblox_localization_tables_api_modified_entry import RobloxLocalizationTablesApiModifiedEntry

        d = dict(src_dict)
        _failed_entries_and_translations = d.pop("failedEntriesAndTranslations", UNSET)
        failed_entries_and_translations: list[RobloxLocalizationTablesApiFailedEntry] | Unset = UNSET
        if _failed_entries_and_translations is not UNSET:
            failed_entries_and_translations = []
            for failed_entries_and_translations_item_data in _failed_entries_and_translations:
                failed_entries_and_translations_item = RobloxLocalizationTablesApiFailedEntry.from_dict(
                    failed_entries_and_translations_item_data
                )

                failed_entries_and_translations.append(failed_entries_and_translations_item)

        _modified_entries_and_translations = d.pop("modifiedEntriesAndTranslations", UNSET)
        modified_entries_and_translations: list[RobloxLocalizationTablesApiModifiedEntry] | Unset = UNSET
        if _modified_entries_and_translations is not UNSET:
            modified_entries_and_translations = []
            for modified_entries_and_translations_item_data in _modified_entries_and_translations:
                modified_entries_and_translations_item = RobloxLocalizationTablesApiModifiedEntry.from_dict(
                    modified_entries_and_translations_item_data
                )

                modified_entries_and_translations.append(modified_entries_and_translations_item)

        roblox_localization_tables_api_update_table_contents_response = cls(
            failed_entries_and_translations=failed_entries_and_translations,
            modified_entries_and_translations=modified_entries_and_translations,
        )

        return roblox_localization_tables_api_update_table_contents_response
