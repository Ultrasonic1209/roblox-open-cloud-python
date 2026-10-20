from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest:
    """
    Attributes:
        is_silent_upgrade (bool | Unset):
    """

    is_silent_upgrade: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_silent_upgrade = self.is_silent_upgrade

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_silent_upgrade is not UNSET:
            field_dict["isSilentUpgrade"] = is_silent_upgrade

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_silent_upgrade = d.pop("isSilentUpgrade", UNSET)

        roblox_authentication_api_models_request_start_passkey_registration_request = cls(
            is_silent_upgrade=is_silent_upgrade,
        )

        return roblox_authentication_api_models_request_start_passkey_registration_request
