from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseMobileClientVersionResponseData")


@_attrs_define
class RobloxClientSettingsApiModelsResponseMobileClientVersionResponseData:
    """
    Attributes:
        upgrade_action (str | Unset):
    """

    upgrade_action: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        upgrade_action = self.upgrade_action

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if upgrade_action is not UNSET:
            field_dict["UpgradeAction"] = upgrade_action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        upgrade_action = d.pop("UpgradeAction", UNSET)

        roblox_client_settings_api_models_response_mobile_client_version_response_data = cls(
            upgrade_action=upgrade_action,
        )

        return roblox_client_settings_api_models_response_mobile_client_version_response_data
