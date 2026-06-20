from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiGameAutolocalizationInformationResponse")


@_attrs_define
class RobloxLocalizationTablesApiGameAutolocalizationInformationResponse:
    """
    Attributes:
        is_autolocalization_enabled (bool | Unset):
        is_automatic_entries_setting_enabled (bool | Unset):
        is_automatic_entries_deletion_enabled (bool | Unset):
        should_use_localization_table (bool | Unset):
        auto_localization_table_id (UUID | Unset):
        source_language (str | Unset):
        asset_id (int | Unset):
    """

    is_autolocalization_enabled: bool | Unset = UNSET
    is_automatic_entries_setting_enabled: bool | Unset = UNSET
    is_automatic_entries_deletion_enabled: bool | Unset = UNSET
    should_use_localization_table: bool | Unset = UNSET
    auto_localization_table_id: UUID | Unset = UNSET
    source_language: str | Unset = UNSET
    asset_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_autolocalization_enabled = self.is_autolocalization_enabled

        is_automatic_entries_setting_enabled = self.is_automatic_entries_setting_enabled

        is_automatic_entries_deletion_enabled = self.is_automatic_entries_deletion_enabled

        should_use_localization_table = self.should_use_localization_table

        auto_localization_table_id: str | Unset = UNSET
        if not isinstance(self.auto_localization_table_id, Unset):
            auto_localization_table_id = str(self.auto_localization_table_id)

        source_language = self.source_language

        asset_id = self.asset_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_autolocalization_enabled is not UNSET:
            field_dict["isAutolocalizationEnabled"] = is_autolocalization_enabled
        if is_automatic_entries_setting_enabled is not UNSET:
            field_dict["isAutomaticEntriesSettingEnabled"] = is_automatic_entries_setting_enabled
        if is_automatic_entries_deletion_enabled is not UNSET:
            field_dict["isAutomaticEntriesDeletionEnabled"] = is_automatic_entries_deletion_enabled
        if should_use_localization_table is not UNSET:
            field_dict["shouldUseLocalizationTable"] = should_use_localization_table
        if auto_localization_table_id is not UNSET:
            field_dict["autoLocalizationTableId"] = auto_localization_table_id
        if source_language is not UNSET:
            field_dict["sourceLanguage"] = source_language
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_autolocalization_enabled = d.pop("isAutolocalizationEnabled", UNSET)

        is_automatic_entries_setting_enabled = d.pop("isAutomaticEntriesSettingEnabled", UNSET)

        is_automatic_entries_deletion_enabled = d.pop("isAutomaticEntriesDeletionEnabled", UNSET)

        should_use_localization_table = d.pop("shouldUseLocalizationTable", UNSET)

        _auto_localization_table_id = d.pop("autoLocalizationTableId", UNSET)
        auto_localization_table_id: UUID | Unset
        if isinstance(_auto_localization_table_id, Unset):
            auto_localization_table_id = UNSET
        else:
            auto_localization_table_id = UUID(_auto_localization_table_id)

        source_language = d.pop("sourceLanguage", UNSET)

        asset_id = d.pop("assetId", UNSET)

        roblox_localization_tables_api_game_autolocalization_information_response = cls(
            is_autolocalization_enabled=is_autolocalization_enabled,
            is_automatic_entries_setting_enabled=is_automatic_entries_setting_enabled,
            is_automatic_entries_deletion_enabled=is_automatic_entries_deletion_enabled,
            should_use_localization_table=should_use_localization_table,
            auto_localization_table_id=auto_localization_table_id,
            source_language=source_language,
            asset_id=asset_id,
        )

        return roblox_localization_tables_api_game_autolocalization_information_response
