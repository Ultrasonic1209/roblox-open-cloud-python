from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_request_external_signup_request_identity_provider_platform_type import (
    RobloxAuthenticationApiModelsRequestExternalSignupRequestIdentityProviderPlatformType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_external_signup_request_additional_info_payload import (
        RobloxAuthenticationApiModelsRequestExternalSignupRequestAdditionalInfoPayload,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestExternalSignupRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestExternalSignupRequest:
    """
    Attributes:
        username (str | Unset):
        password (str | Unset):
        birthday (datetime.datetime | Unset):
        locale (str | Unset):
        authentication_proof (str | Unset):
        identity_provider_platform_type
            (RobloxAuthenticationApiModelsRequestExternalSignupRequestIdentityProviderPlatformType | Unset):  ['Undefined' =
            0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3]
        additional_info_payload (RobloxAuthenticationApiModelsRequestExternalSignupRequestAdditionalInfoPayload |
            Unset):
    """

    username: str | Unset = UNSET
    password: str | Unset = UNSET
    birthday: datetime.datetime | Unset = UNSET
    locale: str | Unset = UNSET
    authentication_proof: str | Unset = UNSET
    identity_provider_platform_type: (
        RobloxAuthenticationApiModelsRequestExternalSignupRequestIdentityProviderPlatformType | Unset
    ) = UNSET
    additional_info_payload: RobloxAuthenticationApiModelsRequestExternalSignupRequestAdditionalInfoPayload | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        birthday: str | Unset = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        locale = self.locale

        authentication_proof = self.authentication_proof

        identity_provider_platform_type: int | Unset = UNSET
        if not isinstance(self.identity_provider_platform_type, Unset):
            identity_provider_platform_type = self.identity_provider_platform_type.value

        additional_info_payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_info_payload, Unset):
            additional_info_payload = self.additional_info_payload.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if locale is not UNSET:
            field_dict["locale"] = locale
        if authentication_proof is not UNSET:
            field_dict["authenticationProof"] = authentication_proof
        if identity_provider_platform_type is not UNSET:
            field_dict["IdentityProviderPlatformType"] = identity_provider_platform_type
        if additional_info_payload is not UNSET:
            field_dict["additionalInfoPayload"] = additional_info_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_external_signup_request_additional_info_payload import (
            RobloxAuthenticationApiModelsRequestExternalSignupRequestAdditionalInfoPayload,
        )

        d = dict(src_dict)
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: datetime.datetime | Unset
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = datetime.datetime.fromisoformat(_birthday)

        locale = d.pop("locale", UNSET)

        authentication_proof = d.pop("authenticationProof", UNSET)

        _identity_provider_platform_type = d.pop("IdentityProviderPlatformType", UNSET)
        identity_provider_platform_type: (
            RobloxAuthenticationApiModelsRequestExternalSignupRequestIdentityProviderPlatformType | Unset
        )
        if isinstance(_identity_provider_platform_type, Unset):
            identity_provider_platform_type = UNSET
        else:
            identity_provider_platform_type = (
                RobloxAuthenticationApiModelsRequestExternalSignupRequestIdentityProviderPlatformType(
                    _identity_provider_platform_type
                )
            )

        _additional_info_payload = d.pop("additionalInfoPayload", UNSET)
        additional_info_payload: RobloxAuthenticationApiModelsRequestExternalSignupRequestAdditionalInfoPayload | Unset
        if isinstance(_additional_info_payload, Unset):
            additional_info_payload = UNSET
        else:
            additional_info_payload = (
                RobloxAuthenticationApiModelsRequestExternalSignupRequestAdditionalInfoPayload.from_dict(
                    _additional_info_payload
                )
            )

        roblox_authentication_api_models_request_external_signup_request = cls(
            username=username,
            password=password,
            birthday=birthday,
            locale=locale,
            authentication_proof=authentication_proof,
            identity_provider_platform_type=identity_provider_platform_type,
            additional_info_payload=additional_info_payload,
        )

        return roblox_authentication_api_models_request_external_signup_request
