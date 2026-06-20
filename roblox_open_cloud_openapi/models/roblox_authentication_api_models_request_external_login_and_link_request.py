from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_request_external_login_and_link_request_ctype import (
    RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestCtype,
)
from ..models.roblox_authentication_api_models_request_external_login_and_link_request_identity_provider_platform_type import (
    RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestIdentityProviderPlatformType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_external_login_and_link_request_additional_info_payload import (
        RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestAdditionalInfoPayload,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest:
    """
    Attributes:
        ctype (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestCtype | Unset):  ['Email' = 0, 'Username'
            = 1, 'PhoneNumber' = 2, 'EmailOtpSessionToken' = 3, 'AuthToken' = 4, 'Passkey' = 5, 'AsUser' = 6,
            'TwoStepVerification' = 7, 'XboxLive' = 8, 'PlatformLive' = 9]
        cvalue (str | Unset):
        password (str | Unset):
        authentication_proof (str | Unset):
        identity_provider_platform_type
            (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestIdentityProviderPlatformType | Unset):
            ['Undefined' = 0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3]
        additional_info_payload (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestAdditionalInfoPayload |
            Unset):
    """

    ctype: RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestCtype | Unset = UNSET
    cvalue: str | Unset = UNSET
    password: str | Unset = UNSET
    authentication_proof: str | Unset = UNSET
    identity_provider_platform_type: (
        RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestIdentityProviderPlatformType | Unset
    ) = UNSET
    additional_info_payload: (
        RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestAdditionalInfoPayload | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        ctype: int | Unset = UNSET
        if not isinstance(self.ctype, Unset):
            ctype = self.ctype.value

        cvalue = self.cvalue

        password = self.password

        authentication_proof = self.authentication_proof

        identity_provider_platform_type: int | Unset = UNSET
        if not isinstance(self.identity_provider_platform_type, Unset):
            identity_provider_platform_type = self.identity_provider_platform_type.value

        additional_info_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_info_payload, Unset):
            additional_info_payload = self.additional_info_payload.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ctype is not UNSET:
            field_dict["ctype"] = ctype
        if cvalue is not UNSET:
            field_dict["cvalue"] = cvalue
        if password is not UNSET:
            field_dict["password"] = password
        if authentication_proof is not UNSET:
            field_dict["authenticationProof"] = authentication_proof
        if identity_provider_platform_type is not UNSET:
            field_dict["IdentityProviderPlatformType"] = identity_provider_platform_type
        if additional_info_payload is not UNSET:
            field_dict["additionalInfoPayload"] = additional_info_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_external_login_and_link_request_additional_info_payload import (
            RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestAdditionalInfoPayload,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _ctype = d.pop("ctype", UNSET)
        ctype: RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestCtype | Unset
        if isinstance(_ctype, Unset):
            ctype = UNSET
        else:
            ctype = RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestCtype(_ctype)

        cvalue = d.pop("cvalue", UNSET)

        password = d.pop("password", UNSET)

        authentication_proof = d.pop("authenticationProof", UNSET)

        _identity_provider_platform_type = d.pop("IdentityProviderPlatformType", UNSET)
        identity_provider_platform_type: (
            RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestIdentityProviderPlatformType | Unset
        )
        if isinstance(_identity_provider_platform_type, Unset):
            identity_provider_platform_type = UNSET
        else:
            identity_provider_platform_type = (
                RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestIdentityProviderPlatformType(
                    _identity_provider_platform_type
                )
            )

        _additional_info_payload = d.pop("additionalInfoPayload", UNSET)
        additional_info_payload: (
            RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestAdditionalInfoPayload | Unset
        )
        if isinstance(_additional_info_payload, Unset):
            additional_info_payload = UNSET
        else:
            additional_info_payload = (
                RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequestAdditionalInfoPayload.from_dict(
                    _additional_info_payload
                )
            )

        roblox_authentication_api_models_request_external_login_and_link_request = cls(
            ctype=ctype,
            cvalue=cvalue,
            password=password,
            authentication_proof=authentication_proof,
            identity_provider_platform_type=identity_provider_platform_type,
            additional_info_payload=additional_info_payload,
        )

        return roblox_authentication_api_models_request_external_login_and_link_request
