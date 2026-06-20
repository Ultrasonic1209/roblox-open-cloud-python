from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_localization_client_user_universe_localization_setting_value import (
        RobloxGameLocalizationClientUserUniverseLocalizationSettingValue,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiModelsResponseGetUserLocalizationSettingsForUniverseResponse")


@_attrs_define
class RobloxGameInternationalizationApiModelsResponseGetUserLocalizationSettingsForUniverseResponse:
    """
    Attributes:
        user_universe_localization_setting_value (RobloxGameLocalizationClientUserUniverseLocalizationSettingValue |
            Unset):
    """

    user_universe_localization_setting_value: (
        RobloxGameLocalizationClientUserUniverseLocalizationSettingValue | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_universe_localization_setting_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_universe_localization_setting_value, Unset):
            user_universe_localization_setting_value = self.user_universe_localization_setting_value.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_universe_localization_setting_value is not UNSET:
            field_dict["userUniverseLocalizationSettingValue"] = user_universe_localization_setting_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_localization_client_user_universe_localization_setting_value import (
            RobloxGameLocalizationClientUserUniverseLocalizationSettingValue,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _user_universe_localization_setting_value = d.pop("userUniverseLocalizationSettingValue", UNSET)
        user_universe_localization_setting_value: (
            RobloxGameLocalizationClientUserUniverseLocalizationSettingValue | Unset
        )
        if isinstance(_user_universe_localization_setting_value, Unset):
            user_universe_localization_setting_value = UNSET
        else:
            user_universe_localization_setting_value = (
                RobloxGameLocalizationClientUserUniverseLocalizationSettingValue.from_dict(
                    _user_universe_localization_setting_value
                )
            )

        roblox_game_internationalization_api_models_response_get_user_localization_settings_for_universe_response = cls(
            user_universe_localization_setting_value=user_universe_localization_setting_value,
        )

        return roblox_game_internationalization_api_models_response_get_user_localization_settings_for_universe_response
