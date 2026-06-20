from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_response_passkey_credential import (
        RobloxAuthenticationApiModelsResponsePasskeyCredential,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponseListPasskeyCredentialResponse")


@_attrs_define
class RobloxAuthenticationApiModelsResponseListPasskeyCredentialResponse:
    """
    Attributes:
        credentials (list[RobloxAuthenticationApiModelsResponsePasskeyCredential] | Unset):
    """

    credentials: list[RobloxAuthenticationApiModelsResponsePasskeyCredential] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = []
            for credentials_item_data in self.credentials:
                credentials_item = credentials_item_data.to_dict()
                credentials.append(credentials_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_response_passkey_credential import (
            RobloxAuthenticationApiModelsResponsePasskeyCredential,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _credentials = d.pop("credentials", UNSET)
        credentials: list[RobloxAuthenticationApiModelsResponsePasskeyCredential] | Unset = UNSET
        if _credentials is not UNSET:
            credentials = []
            for credentials_item_data in _credentials:
                credentials_item = RobloxAuthenticationApiModelsResponsePasskeyCredential.from_dict(
                    credentials_item_data
                )

                credentials.append(credentials_item)

        roblox_authentication_api_models_response_list_passkey_credential_response = cls(
            credentials=credentials,
        )

        return roblox_authentication_api_models_response_list_passkey_credential_response
