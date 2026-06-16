from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_password_reset_model_target_type import (
    RobloxAuthenticationApiModelsPasswordResetModelTargetType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
        RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsPasswordResetModel")


@_attrs_define
class RobloxAuthenticationApiModelsPasswordResetModel:
    """
    Attributes:
        target_type (RobloxAuthenticationApiModelsPasswordResetModelTargetType | Unset):  ['Email' = 0, 'PhoneNumber' =
            1, 'RecoverySessionID' = 2]
        ticket (str | Unset):
        user_id (int | Unset):
        password (str | Unset):
        password_repeated (str | Unset):
        two_step_verification_challenge_id (str | Unset):
        two_step_verification_token (str | Unset):
        account_blob (str | Unset):
        secure_authentication_intent (RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset):
        new_email (str | Unset):
        passkey_session_id (str | Unset):
        passkey_registration_response (str | Unset):
    """

    target_type: RobloxAuthenticationApiModelsPasswordResetModelTargetType | Unset = UNSET
    ticket: str | Unset = UNSET
    user_id: int | Unset = UNSET
    password: str | Unset = UNSET
    password_repeated: str | Unset = UNSET
    two_step_verification_challenge_id: str | Unset = UNSET
    two_step_verification_token: str | Unset = UNSET
    account_blob: str | Unset = UNSET
    secure_authentication_intent: RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset = UNSET
    new_email: str | Unset = UNSET
    passkey_session_id: str | Unset = UNSET
    passkey_registration_response: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_type: int | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        ticket = self.ticket

        user_id = self.user_id

        password = self.password

        password_repeated = self.password_repeated

        two_step_verification_challenge_id = self.two_step_verification_challenge_id

        two_step_verification_token = self.two_step_verification_token

        account_blob = self.account_blob

        secure_authentication_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secure_authentication_intent, Unset):
            secure_authentication_intent = self.secure_authentication_intent.to_dict()

        new_email = self.new_email

        passkey_session_id = self.passkey_session_id

        passkey_registration_response = self.passkey_registration_response

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if ticket is not UNSET:
            field_dict["ticket"] = ticket
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if password is not UNSET:
            field_dict["password"] = password
        if password_repeated is not UNSET:
            field_dict["passwordRepeated"] = password_repeated
        if two_step_verification_challenge_id is not UNSET:
            field_dict["twoStepVerificationChallengeId"] = two_step_verification_challenge_id
        if two_step_verification_token is not UNSET:
            field_dict["twoStepVerificationToken"] = two_step_verification_token
        if account_blob is not UNSET:
            field_dict["accountBlob"] = account_blob
        if secure_authentication_intent is not UNSET:
            field_dict["secureAuthenticationIntent"] = secure_authentication_intent
        if new_email is not UNSET:
            field_dict["newEmail"] = new_email
        if passkey_session_id is not UNSET:
            field_dict["passkeySessionId"] = passkey_session_id
        if passkey_registration_response is not UNSET:
            field_dict["passkeyRegistrationResponse"] = passkey_registration_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
            RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
        )

        d = dict(src_dict)
        _target_type = d.pop("targetType", UNSET)
        target_type: RobloxAuthenticationApiModelsPasswordResetModelTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = RobloxAuthenticationApiModelsPasswordResetModelTargetType(_target_type)

        ticket = d.pop("ticket", UNSET)

        user_id = d.pop("userId", UNSET)

        password = d.pop("password", UNSET)

        password_repeated = d.pop("passwordRepeated", UNSET)

        two_step_verification_challenge_id = d.pop("twoStepVerificationChallengeId", UNSET)

        two_step_verification_token = d.pop("twoStepVerificationToken", UNSET)

        account_blob = d.pop("accountBlob", UNSET)

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

        new_email = d.pop("newEmail", UNSET)

        passkey_session_id = d.pop("passkeySessionId", UNSET)

        passkey_registration_response = d.pop("passkeyRegistrationResponse", UNSET)

        roblox_authentication_api_models_password_reset_model = cls(
            target_type=target_type,
            ticket=ticket,
            user_id=user_id,
            password=password,
            password_repeated=password_repeated,
            two_step_verification_challenge_id=two_step_verification_challenge_id,
            two_step_verification_token=two_step_verification_token,
            account_blob=account_blob,
            secure_authentication_intent=secure_authentication_intent,
            new_email=new_email,
            passkey_session_id=passkey_session_id,
            passkey_registration_response=passkey_registration_response,
        )

        return roblox_authentication_api_models_password_reset_model
