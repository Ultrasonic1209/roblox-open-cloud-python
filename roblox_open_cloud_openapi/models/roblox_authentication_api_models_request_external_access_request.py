from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_request_external_access_request_identity_provider_platform_type import (
    RobloxAuthenticationApiModelsRequestExternalAccessRequestIdentityProviderPlatformType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_external_access_request_additional_info_payload import (
        RobloxAuthenticationApiModelsRequestExternalAccessRequestAdditionalInfoPayload,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestExternalAccessRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestExternalAccessRequest:
    """
    Attributes:
        authentication_proof (str | Unset):
        identity_provider_platform_type
            (RobloxAuthenticationApiModelsRequestExternalAccessRequestIdentityProviderPlatformType | Unset):  ['Undefined' =
            0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3]
        additional_info_payload (RobloxAuthenticationApiModelsRequestExternalAccessRequestAdditionalInfoPayload |
            Unset):
    """

    authentication_proof: str | Unset = UNSET
    identity_provider_platform_type: (
        RobloxAuthenticationApiModelsRequestExternalAccessRequestIdentityProviderPlatformType | Unset
    ) = UNSET
    additional_info_payload: RobloxAuthenticationApiModelsRequestExternalAccessRequestAdditionalInfoPayload | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        authentication_proof = self.authentication_proof

        identity_provider_platform_type: int | Unset = UNSET
        if not isinstance(self.identity_provider_platform_type, Unset):
            identity_provider_platform_type = self.identity_provider_platform_type.value

        additional_info_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_info_payload, Unset):
            additional_info_payload = self.additional_info_payload.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if authentication_proof is not UNSET:
            field_dict["authenticationProof"] = authentication_proof
        if identity_provider_platform_type is not UNSET:
            field_dict["identityProviderPlatformType"] = identity_provider_platform_type
        if additional_info_payload is not UNSET:
            field_dict["additionalInfoPayload"] = additional_info_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_external_access_request_additional_info_payload import (
            RobloxAuthenticationApiModelsRequestExternalAccessRequestAdditionalInfoPayload,
        )

        d = dict(src_dict)
        authentication_proof = d.pop("authenticationProof", UNSET)

        _identity_provider_platform_type = d.pop("identityProviderPlatformType", UNSET)
        identity_provider_platform_type: (
            RobloxAuthenticationApiModelsRequestExternalAccessRequestIdentityProviderPlatformType | Unset
        )
        if isinstance(_identity_provider_platform_type, Unset):
            identity_provider_platform_type = UNSET
        else:
            identity_provider_platform_type = (
                RobloxAuthenticationApiModelsRequestExternalAccessRequestIdentityProviderPlatformType(
                    _identity_provider_platform_type
                )
            )

        _additional_info_payload = d.pop("additionalInfoPayload", UNSET)
        additional_info_payload: RobloxAuthenticationApiModelsRequestExternalAccessRequestAdditionalInfoPayload | Unset
        if isinstance(_additional_info_payload, Unset):
            additional_info_payload = UNSET
        else:
            additional_info_payload = (
                RobloxAuthenticationApiModelsRequestExternalAccessRequestAdditionalInfoPayload.from_dict(
                    _additional_info_payload
                )
            )

        roblox_authentication_api_models_request_external_access_request = cls(
            authentication_proof=authentication_proof,
            identity_provider_platform_type=identity_provider_platform_type,
            additional_info_payload=additional_info_payload,
        )

        return roblox_authentication_api_models_request_external_access_request
