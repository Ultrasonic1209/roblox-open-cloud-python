from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel")


@_attrs_define
class RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel:
    """
    Attributes:
        client_public_key (str | Unset):
        client_epoch_timestamp (int | Unset):
        sai_signature (str | Unset):
        server_nonce (str | Unset):
    """

    client_public_key: str | Unset = UNSET
    client_epoch_timestamp: int | Unset = UNSET
    sai_signature: str | Unset = UNSET
    server_nonce: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_public_key = self.client_public_key

        client_epoch_timestamp = self.client_epoch_timestamp

        sai_signature = self.sai_signature

        server_nonce = self.server_nonce

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if client_public_key is not UNSET:
            field_dict["clientPublicKey"] = client_public_key
        if client_epoch_timestamp is not UNSET:
            field_dict["clientEpochTimestamp"] = client_epoch_timestamp
        if sai_signature is not UNSET:
            field_dict["saiSignature"] = sai_signature
        if server_nonce is not UNSET:
            field_dict["serverNonce"] = server_nonce

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_public_key = d.pop("clientPublicKey", UNSET)

        client_epoch_timestamp = d.pop("clientEpochTimestamp", UNSET)

        sai_signature = d.pop("saiSignature", UNSET)

        server_nonce = d.pop("serverNonce", UNSET)

        roblox_authentication_api_models_request_secure_authentication_intent_model = cls(
            client_public_key=client_public_key,
            client_epoch_timestamp=client_epoch_timestamp,
            sai_signature=sai_signature,
            server_nonce=server_nonce,
        )

        return roblox_authentication_api_models_request_secure_authentication_intent_model
