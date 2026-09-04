from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse")


@_attrs_define
class RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse:
    """
    Attributes:
        nonce (str | Unset):
    """

    nonce: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        nonce = self.nonce

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if nonce is not UNSET:
            field_dict["nonce"] = nonce

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        nonce = d.pop("nonce", UNSET)

        roblox_authentication_api_models_response_external_identity_gateway_external_identity_nonce_response = cls(
            nonce=nonce,
        )

        return roblox_authentication_api_models_response_external_identity_gateway_external_identity_nonce_response
