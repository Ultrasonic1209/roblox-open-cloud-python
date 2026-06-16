from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse")


@_attrs_define
class RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse:
    """ """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        roblox_account_settings_api_models_response_update_account_country_response = cls()

        return roblox_account_settings_api_models_response_update_account_country_response
