from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiGameAutolocalizationInformationResponse")


@_attrs_define
class RobloxGameInternationalizationApiGameAutolocalizationInformationResponse:
    """
    Attributes:
        is_autolocalization_enabled (bool | Unset):
        should_use_localization_table (bool | Unset):
        auto_localization_table_id (UUID | Unset):
        asset_id (int | Unset):
    """

    is_autolocalization_enabled: bool | Unset = UNSET
    should_use_localization_table: bool | Unset = UNSET
    auto_localization_table_id: UUID | Unset = UNSET
    asset_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_autolocalization_enabled = self.is_autolocalization_enabled

        should_use_localization_table = self.should_use_localization_table

        auto_localization_table_id: str | Unset = UNSET
        if not isinstance(self.auto_localization_table_id, Unset):
            auto_localization_table_id = str(self.auto_localization_table_id)

        asset_id = self.asset_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_autolocalization_enabled is not UNSET:
            field_dict["isAutolocalizationEnabled"] = is_autolocalization_enabled
        if should_use_localization_table is not UNSET:
            field_dict["shouldUseLocalizationTable"] = should_use_localization_table
        if auto_localization_table_id is not UNSET:
            field_dict["autoLocalizationTableId"] = auto_localization_table_id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_autolocalization_enabled = d.pop("isAutolocalizationEnabled", UNSET)

        should_use_localization_table = d.pop("shouldUseLocalizationTable", UNSET)

        _auto_localization_table_id = d.pop("autoLocalizationTableId", UNSET)
        auto_localization_table_id: UUID | Unset
        if isinstance(_auto_localization_table_id, Unset):
            auto_localization_table_id = UNSET
        else:
            auto_localization_table_id = UUID(_auto_localization_table_id)

        asset_id = d.pop("assetId", UNSET)

        roblox_game_internationalization_api_game_autolocalization_information_response = cls(
            is_autolocalization_enabled=is_autolocalization_enabled,
            should_use_localization_table=should_use_localization_table,
            auto_localization_table_id=auto_localization_table_id,
            asset_id=asset_id,
        )

        return roblox_game_internationalization_api_game_autolocalization_information_response
