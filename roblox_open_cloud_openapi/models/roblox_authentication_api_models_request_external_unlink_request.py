from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_request_external_unlink_request_identity_provider_platform_type import (
    RobloxAuthenticationApiModelsRequestExternalUnlinkRequestIdentityProviderPlatformType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_external_unlink_request_additional_info_payload import (
        RobloxAuthenticationApiModelsRequestExternalUnlinkRequestAdditionalInfoPayload,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestExternalUnlinkRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestExternalUnlinkRequest:
    """
    Attributes:
        identity_provider_platform_type
            (RobloxAuthenticationApiModelsRequestExternalUnlinkRequestIdentityProviderPlatformType | Unset):  ['Undefined' =
            0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3]
        additional_info_payload (RobloxAuthenticationApiModelsRequestExternalUnlinkRequestAdditionalInfoPayload |
            Unset):
    """

    identity_provider_platform_type: (
        RobloxAuthenticationApiModelsRequestExternalUnlinkRequestIdentityProviderPlatformType | Unset
    ) = UNSET
    additional_info_payload: RobloxAuthenticationApiModelsRequestExternalUnlinkRequestAdditionalInfoPayload | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        identity_provider_platform_type: int | Unset = UNSET
        if not isinstance(self.identity_provider_platform_type, Unset):
            identity_provider_platform_type = self.identity_provider_platform_type.value

        additional_info_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_info_payload, Unset):
            additional_info_payload = self.additional_info_payload.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if identity_provider_platform_type is not UNSET:
            field_dict["IdentityProviderPlatformType"] = identity_provider_platform_type
        if additional_info_payload is not UNSET:
            field_dict["additionalInfoPayload"] = additional_info_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_external_unlink_request_additional_info_payload import (
            RobloxAuthenticationApiModelsRequestExternalUnlinkRequestAdditionalInfoPayload,
        )

        d = dict(src_dict)
        _identity_provider_platform_type = d.pop("IdentityProviderPlatformType", UNSET)
        identity_provider_platform_type: (
            RobloxAuthenticationApiModelsRequestExternalUnlinkRequestIdentityProviderPlatformType | Unset
        )
        if isinstance(_identity_provider_platform_type, Unset):
            identity_provider_platform_type = UNSET
        else:
            identity_provider_platform_type = (
                RobloxAuthenticationApiModelsRequestExternalUnlinkRequestIdentityProviderPlatformType(
                    _identity_provider_platform_type
                )
            )

        _additional_info_payload = d.pop("additionalInfoPayload", UNSET)
        additional_info_payload: RobloxAuthenticationApiModelsRequestExternalUnlinkRequestAdditionalInfoPayload | Unset
        if isinstance(_additional_info_payload, Unset):
            additional_info_payload = UNSET
        else:
            additional_info_payload = (
                RobloxAuthenticationApiModelsRequestExternalUnlinkRequestAdditionalInfoPayload.from_dict(
                    _additional_info_payload
                )
            )

        roblox_authentication_api_models_request_external_unlink_request = cls(
            identity_provider_platform_type=identity_provider_platform_type,
            additional_info_payload=additional_info_payload,
        )

        return roblox_authentication_api_models_request_external_unlink_request
