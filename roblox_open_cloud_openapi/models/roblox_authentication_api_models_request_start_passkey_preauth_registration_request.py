from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest:
    """
    Attributes:
        username (str | Unset):
    """

    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        username = d.pop("username", UNSET)

        roblox_authentication_api_models_request_start_passkey_preauth_registration_request = cls(
            username=username,
        )

        return roblox_authentication_api_models_request_start_passkey_preauth_registration_request
