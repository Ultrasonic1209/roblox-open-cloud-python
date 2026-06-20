from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_account_settings_api_models_response_user_account_country import (
        RobloxAccountSettingsApiModelsResponseUserAccountCountry,
    )


T = TypeVar("T", bound="RobloxAccountSettingsApiModelsResponseAccountCountrySettingsResponse")


@_attrs_define
class RobloxAccountSettingsApiModelsResponseAccountCountrySettingsResponse:
    """
    Attributes:
        value (RobloxAccountSettingsApiModelsResponseUserAccountCountry | Unset):
    """

    value: RobloxAccountSettingsApiModelsResponseUserAccountCountry | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_account_settings_api_models_response_user_account_country import (
            RobloxAccountSettingsApiModelsResponseUserAccountCountry,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _value = d.pop("value", UNSET)
        value: RobloxAccountSettingsApiModelsResponseUserAccountCountry | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = RobloxAccountSettingsApiModelsResponseUserAccountCountry.from_dict(_value)

        roblox_account_settings_api_models_response_account_country_settings_response = cls(
            value=value,
        )

        return roblox_account_settings_api_models_response_account_country_settings_response
