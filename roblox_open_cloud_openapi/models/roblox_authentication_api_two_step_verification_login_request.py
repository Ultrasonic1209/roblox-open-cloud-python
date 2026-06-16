from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_account_link_parameters import (
        RobloxAuthenticationApiModelsAccountLinkParameters,
    )
    from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
        RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiTwoStepVerificationLoginRequest")


@_attrs_define
class RobloxAuthenticationApiTwoStepVerificationLoginRequest:
    """
    Attributes:
        challenge_id (str | Unset):
        verification_token (str | Unset):
        remember_device (bool | Unset):
        secure_authentication_intent (RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset):
        account_blob (str | Unset):
        account_link_parameters (RobloxAuthenticationApiModelsAccountLinkParameters | Unset):
    """

    challenge_id: str | Unset = UNSET
    verification_token: str | Unset = UNSET
    remember_device: bool | Unset = UNSET
    secure_authentication_intent: RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset = UNSET
    account_blob: str | Unset = UNSET
    account_link_parameters: RobloxAuthenticationApiModelsAccountLinkParameters | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        challenge_id = self.challenge_id

        verification_token = self.verification_token

        remember_device = self.remember_device

        secure_authentication_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secure_authentication_intent, Unset):
            secure_authentication_intent = self.secure_authentication_intent.to_dict()

        account_blob = self.account_blob

        account_link_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_link_parameters, Unset):
            account_link_parameters = self.account_link_parameters.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if challenge_id is not UNSET:
            field_dict["challengeId"] = challenge_id
        if verification_token is not UNSET:
            field_dict["verificationToken"] = verification_token
        if remember_device is not UNSET:
            field_dict["rememberDevice"] = remember_device
        if secure_authentication_intent is not UNSET:
            field_dict["secureAuthenticationIntent"] = secure_authentication_intent
        if account_blob is not UNSET:
            field_dict["accountBlob"] = account_blob
        if account_link_parameters is not UNSET:
            field_dict["accountLinkParameters"] = account_link_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_account_link_parameters import (
            RobloxAuthenticationApiModelsAccountLinkParameters,
        )
        from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
            RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
        )

        d = dict(src_dict)
        challenge_id = d.pop("challengeId", UNSET)

        verification_token = d.pop("verificationToken", UNSET)

        remember_device = d.pop("rememberDevice", UNSET)

        _secure_authentication_intent = d.pop("secureAuthenticationIntent", UNSET)
        secure_authentication_intent: RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset
        if isinstance(_secure_authentication_intent, Unset):
            secure_authentication_intent = UNSET
        else:
            secure_authentication_intent = (
                RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel.from_dict(
                    _secure_authentication_intent
                )
            )

        account_blob = d.pop("accountBlob", UNSET)

        _account_link_parameters = d.pop("accountLinkParameters", UNSET)
        account_link_parameters: RobloxAuthenticationApiModelsAccountLinkParameters | Unset
        if isinstance(_account_link_parameters, Unset):
            account_link_parameters = UNSET
        else:
            account_link_parameters = RobloxAuthenticationApiModelsAccountLinkParameters.from_dict(
                _account_link_parameters
            )

        roblox_authentication_api_two_step_verification_login_request = cls(
            challenge_id=challenge_id,
            verification_token=verification_token,
            remember_device=remember_device,
            secure_authentication_intent=secure_authentication_intent,
            account_blob=account_blob,
            account_link_parameters=account_link_parameters,
        )

        return roblox_authentication_api_two_step_verification_login_request
