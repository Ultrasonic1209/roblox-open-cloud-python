from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest")


@_attrs_define
class RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest:
    """
    Attributes:
        is_autolocalization_enabled (bool | Unset):
        should_use_localization_table (bool | Unset):
    """

    is_autolocalization_enabled: bool | Unset = UNSET
    should_use_localization_table: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_autolocalization_enabled = self.is_autolocalization_enabled

        should_use_localization_table = self.should_use_localization_table

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_autolocalization_enabled is not UNSET:
            field_dict["isAutolocalizationEnabled"] = is_autolocalization_enabled
        if should_use_localization_table is not UNSET:
            field_dict["shouldUseLocalizationTable"] = should_use_localization_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_autolocalization_enabled = d.pop("isAutolocalizationEnabled", UNSET)

        should_use_localization_table = d.pop("shouldUseLocalizationTable", UNSET)

        roblox_game_internationalization_api_set_autolocalization_settings_for_game_request = cls(
            is_autolocalization_enabled=is_autolocalization_enabled,
            should_use_localization_table=should_use_localization_table,
        )

        return roblox_game_internationalization_api_set_autolocalization_settings_for_game_request
