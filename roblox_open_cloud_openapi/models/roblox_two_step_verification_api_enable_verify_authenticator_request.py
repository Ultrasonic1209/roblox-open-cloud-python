from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_two_step_verification_api_models_request_secure_authentication_intent_model import (
        RobloxTwoStepVerificationApiModelsRequestSecureAuthenticationIntentModel,
    )


T = TypeVar("T", bound="RobloxTwoStepVerificationApiEnableVerifyAuthenticatorRequest")


@_attrs_define
class RobloxTwoStepVerificationApiEnableVerifyAuthenticatorRequest:
    """Request parameters for authenticator enabling-verify.

    Attributes:
        setup_token (str | Unset): The setup token from the enable authenticator request.
        code (str | Unset): The code from the authenticator app.
        password (str | Unset): The user's password.
        secure_authentication_intent (RobloxTwoStepVerificationApiModelsRequestSecureAuthenticationIntentModel | Unset):
            Model describing secure auth intent.
    """

    setup_token: str | Unset = UNSET
    code: str | Unset = UNSET
    password: str | Unset = UNSET
    secure_authentication_intent: RobloxTwoStepVerificationApiModelsRequestSecureAuthenticationIntentModel | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        setup_token = self.setup_token

        code = self.code

        password = self.password

        secure_authentication_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secure_authentication_intent, Unset):
            secure_authentication_intent = self.secure_authentication_intent.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if setup_token is not UNSET:
            field_dict["setupToken"] = setup_token
        if code is not UNSET:
            field_dict["code"] = code
        if password is not UNSET:
            field_dict["password"] = password
        if secure_authentication_intent is not UNSET:
            field_dict["secureAuthenticationIntent"] = secure_authentication_intent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_two_step_verification_api_models_request_secure_authentication_intent_model import (
            RobloxTwoStepVerificationApiModelsRequestSecureAuthenticationIntentModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        setup_token = d.pop("setupToken", UNSET)

        code = d.pop("code", UNSET)

        password = d.pop("password", UNSET)

        _secure_authentication_intent = d.pop("secureAuthenticationIntent", UNSET)
        secure_authentication_intent: RobloxTwoStepVerificationApiModelsRequestSecureAuthenticationIntentModel | Unset
        if isinstance(_secure_authentication_intent, Unset):
            secure_authentication_intent = UNSET
        else:
            secure_authentication_intent = (
                RobloxTwoStepVerificationApiModelsRequestSecureAuthenticationIntentModel.from_dict(
                    _secure_authentication_intent
                )
            )

        roblox_two_step_verification_api_enable_verify_authenticator_request = cls(
            setup_token=setup_token,
            code=code,
            password=password,
            secure_authentication_intent=secure_authentication_intent,
        )

        return roblox_two_step_verification_api_enable_verify_authenticator_request
