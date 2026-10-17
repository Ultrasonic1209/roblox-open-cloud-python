from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_game_localization_client_user_universe_localization_setting_value_setting_type import (
    RobloxGameLocalizationClientUserUniverseLocalizationSettingValueSettingType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameLocalizationClientUserUniverseLocalizationSettingValue")


@_attrs_define
class RobloxGameLocalizationClientUserUniverseLocalizationSettingValue:
    """
    Attributes:
        setting_type (RobloxGameLocalizationClientUserUniverseLocalizationSettingValueSettingType | Unset):
            ['LanguageFamily' = 0, 'SupportedLocale' = 1, 'SourceOrTranslation' = 2]
        setting_target_id (int | Unset):
        setting_target_code (str | Unset):
    """

    setting_type: RobloxGameLocalizationClientUserUniverseLocalizationSettingValueSettingType | Unset = UNSET
    setting_target_id: int | Unset = UNSET
    setting_target_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        setting_type: str | Unset = UNSET
        if not isinstance(self.setting_type, Unset):
            setting_type = self.setting_type.value

        setting_target_id = self.setting_target_id

        setting_target_code = self.setting_target_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if setting_type is not UNSET:
            field_dict["settingType"] = setting_type
        if setting_target_id is not UNSET:
            field_dict["settingTargetId"] = setting_target_id
        if setting_target_code is not UNSET:
            field_dict["settingTargetCode"] = setting_target_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _setting_type = d.pop("settingType", UNSET)
        setting_type: RobloxGameLocalizationClientUserUniverseLocalizationSettingValueSettingType | Unset
        if isinstance(_setting_type, Unset):
            setting_type = UNSET
        else:
            setting_type = RobloxGameLocalizationClientUserUniverseLocalizationSettingValueSettingType(_setting_type)

        setting_target_id = d.pop("settingTargetId", UNSET)

        setting_target_code = d.pop("settingTargetCode", UNSET)

        roblox_game_localization_client_user_universe_localization_setting_value = cls(
            setting_type=setting_type,
            setting_target_id=setting_target_id,
            setting_target_code=setting_target_code,
        )

        return roblox_game_localization_client_user_universe_localization_setting_value
