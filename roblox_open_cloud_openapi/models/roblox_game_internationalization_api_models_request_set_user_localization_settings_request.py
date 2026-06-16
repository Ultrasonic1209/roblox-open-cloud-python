from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_localization_client_user_universe_localization_setting_value import (
        RobloxGameLocalizationClientUserUniverseLocalizationSettingValue,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest")


@_attrs_define
class RobloxGameInternationalizationApiModelsRequestSetUserLocalizationSettingsRequest:
    """
    Attributes:
        setting_value (RobloxGameLocalizationClientUserUniverseLocalizationSettingValue | Unset):
    """

    setting_value: RobloxGameLocalizationClientUserUniverseLocalizationSettingValue | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        setting_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.setting_value, Unset):
            setting_value = self.setting_value.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if setting_value is not UNSET:
            field_dict["settingValue"] = setting_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_localization_client_user_universe_localization_setting_value import (
            RobloxGameLocalizationClientUserUniverseLocalizationSettingValue,
        )

        d = dict(src_dict)
        _setting_value = d.pop("settingValue", UNSET)
        setting_value: RobloxGameLocalizationClientUserUniverseLocalizationSettingValue | Unset
        if isinstance(_setting_value, Unset):
            setting_value = UNSET
        else:
            setting_value = RobloxGameLocalizationClientUserUniverseLocalizationSettingValue.from_dict(_setting_value)

        roblox_game_internationalization_api_models_request_set_user_localization_settings_request = cls(
            setting_value=setting_value,
        )

        return roblox_game_internationalization_api_models_request_set_user_localization_settings_request
