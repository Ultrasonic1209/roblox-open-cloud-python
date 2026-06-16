from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_client_settings_api_models_response_mobile_client_version_response_data import (
        RobloxClientSettingsApiModelsResponseMobileClientVersionResponseData,
    )


T = TypeVar("T", bound="RobloxClientSettingsApiModelsResponseMobileClientVersionResponse")


@_attrs_define
class RobloxClientSettingsApiModelsResponseMobileClientVersionResponse:
    """
    Attributes:
        active_version (str | Unset):
        upgrade_source (str | Unset):
        md5_sum (str | Unset):
        data (RobloxClientSettingsApiModelsResponseMobileClientVersionResponseData | Unset):
    """

    active_version: str | Unset = UNSET
    upgrade_source: str | Unset = UNSET
    md5_sum: str | Unset = UNSET
    data: RobloxClientSettingsApiModelsResponseMobileClientVersionResponseData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active_version = self.active_version

        upgrade_source = self.upgrade_source

        md5_sum = self.md5_sum

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if active_version is not UNSET:
            field_dict["activeVersion"] = active_version
        if upgrade_source is not UNSET:
            field_dict["upgradeSource"] = upgrade_source
        if md5_sum is not UNSET:
            field_dict["MD5Sum"] = md5_sum
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_client_settings_api_models_response_mobile_client_version_response_data import (
            RobloxClientSettingsApiModelsResponseMobileClientVersionResponseData,
        )

        d = dict(src_dict)
        active_version = d.pop("activeVersion", UNSET)

        upgrade_source = d.pop("upgradeSource", UNSET)

        md5_sum = d.pop("MD5Sum", UNSET)

        _data = d.pop("data", UNSET)
        data: RobloxClientSettingsApiModelsResponseMobileClientVersionResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RobloxClientSettingsApiModelsResponseMobileClientVersionResponseData.from_dict(_data)

        roblox_client_settings_api_models_response_mobile_client_version_response = cls(
            active_version=active_version,
            upgrade_source=upgrade_source,
            md5_sum=md5_sum,
            data=data,
        )

        return roblox_client_settings_api_models_response_mobile_client_version_response
