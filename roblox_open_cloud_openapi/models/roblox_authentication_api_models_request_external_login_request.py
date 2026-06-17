from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_request_external_login_request_identity_provider import (
    RobloxAuthenticationApiModelsRequestExternalLoginRequestIdentityProvider,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_external_login_request_additional_data import (
        RobloxAuthenticationApiModelsRequestExternalLoginRequestAdditionalData,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestExternalLoginRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestExternalLoginRequest:
    """
    Attributes:
        identity_provider (RobloxAuthenticationApiModelsRequestExternalLoginRequestIdentityProvider | Unset):
        additional_data (RobloxAuthenticationApiModelsRequestExternalLoginRequestAdditionalData | Unset):
        authentication_proof (str | Unset):
    """

    identity_provider: RobloxAuthenticationApiModelsRequestExternalLoginRequestIdentityProvider | Unset = UNSET
    additional_data: RobloxAuthenticationApiModelsRequestExternalLoginRequestAdditionalData | Unset = UNSET
    authentication_proof: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        identity_provider: int | Unset = UNSET
        if not isinstance(self.identity_provider, Unset):
            identity_provider = self.identity_provider.value

        additional_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_data, Unset):
            additional_data = self.additional_data.to_dict()

        authentication_proof = self.authentication_proof

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if identity_provider is not UNSET:
            field_dict["identityProvider"] = identity_provider
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data
        if authentication_proof is not UNSET:
            field_dict["authenticationProof"] = authentication_proof

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_external_login_request_additional_data import (
            RobloxAuthenticationApiModelsRequestExternalLoginRequestAdditionalData,
        )

        d = dict(src_dict)
        _identity_provider = d.pop("identityProvider", UNSET)
        identity_provider: RobloxAuthenticationApiModelsRequestExternalLoginRequestIdentityProvider | Unset
        if isinstance(_identity_provider, Unset):
            identity_provider = UNSET
        else:
            identity_provider = RobloxAuthenticationApiModelsRequestExternalLoginRequestIdentityProvider(
                _identity_provider
            )

        _additional_data = d.pop("additionalData", UNSET)
        additional_data: RobloxAuthenticationApiModelsRequestExternalLoginRequestAdditionalData | Unset
        if isinstance(_additional_data, Unset):
            additional_data = UNSET
        else:
            additional_data = RobloxAuthenticationApiModelsRequestExternalLoginRequestAdditionalData.from_dict(
                _additional_data
            )

        authentication_proof = d.pop("authenticationProof", UNSET)

        roblox_authentication_api_models_request_external_login_request = cls(
            identity_provider=identity_provider,
            additional_data=additional_data,
            authentication_proof=authentication_proof,
        )

        return roblox_authentication_api_models_request_external_login_request
