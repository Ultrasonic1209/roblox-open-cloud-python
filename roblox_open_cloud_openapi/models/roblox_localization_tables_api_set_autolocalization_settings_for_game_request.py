from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiSetAutolocalizationSettingsForGameRequest")


@_attrs_define
class RobloxLocalizationTablesApiSetAutolocalizationSettingsForGameRequest:
    """
    Attributes:
        is_autolocalization_enabled (bool | Unset):
        is_automatic_entries_setting_enabled (bool | Unset):
        is_automatic_entries_deletions_enabled (bool | Unset):
        should_use_localization_table (bool | Unset):
    """

    is_autolocalization_enabled: bool | Unset = UNSET
    is_automatic_entries_setting_enabled: bool | Unset = UNSET
    is_automatic_entries_deletions_enabled: bool | Unset = UNSET
    should_use_localization_table: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_autolocalization_enabled = self.is_autolocalization_enabled

        is_automatic_entries_setting_enabled = self.is_automatic_entries_setting_enabled

        is_automatic_entries_deletions_enabled = self.is_automatic_entries_deletions_enabled

        should_use_localization_table = self.should_use_localization_table

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_autolocalization_enabled is not UNSET:
            field_dict["isAutolocalizationEnabled"] = is_autolocalization_enabled
        if is_automatic_entries_setting_enabled is not UNSET:
            field_dict["isAutomaticEntriesSettingEnabled"] = is_automatic_entries_setting_enabled
        if is_automatic_entries_deletions_enabled is not UNSET:
            field_dict["isAutomaticEntriesDeletionsEnabled"] = is_automatic_entries_deletions_enabled
        if should_use_localization_table is not UNSET:
            field_dict["shouldUseLocalizationTable"] = should_use_localization_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_autolocalization_enabled = d.pop("isAutolocalizationEnabled", UNSET)

        is_automatic_entries_setting_enabled = d.pop("isAutomaticEntriesSettingEnabled", UNSET)

        is_automatic_entries_deletions_enabled = d.pop("isAutomaticEntriesDeletionsEnabled", UNSET)

        should_use_localization_table = d.pop("shouldUseLocalizationTable", UNSET)

        roblox_localization_tables_api_set_autolocalization_settings_for_game_request = cls(
            is_autolocalization_enabled=is_autolocalization_enabled,
            is_automatic_entries_setting_enabled=is_automatic_entries_setting_enabled,
            is_automatic_entries_deletions_enabled=is_automatic_entries_deletions_enabled,
            should_use_localization_table=should_use_localization_table,
        )

        return roblox_localization_tables_api_set_autolocalization_settings_for_game_request
