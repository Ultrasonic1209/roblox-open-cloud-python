from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_two_step_verification_sent_response import (
        RobloxAuthenticationApiModelsTwoStepVerificationSentResponse,
    )
    from ..models.roblox_web_responses_users_skinny_user_response import RobloxWebResponsesUsersSkinnyUserResponse


T = TypeVar("T", bound="RobloxAuthenticationApiModelsLoginResponse")


@_attrs_define
class RobloxAuthenticationApiModelsLoginResponse:
    """
    Attributes:
        user (RobloxWebResponsesUsersSkinnyUserResponse | Unset):
        two_step_verification_data (RobloxAuthenticationApiModelsTwoStepVerificationSentResponse | Unset):
        identity_verification_login_ticket (str | Unset):
        is_banned (bool | Unset):
        account_blob (str | Unset):
        should_update_email (bool | Unset):
        recovery_email (str | Unset):
        passkey_registration_succeeded (bool | Unset):
        should_auto_login_from_recovery (bool | Unset):
        should_prompt_2_sv_removal (bool | Unset):
        should_prompt_passkey_addition (bool | Unset):
    """

    user: RobloxWebResponsesUsersSkinnyUserResponse | Unset = UNSET
    two_step_verification_data: RobloxAuthenticationApiModelsTwoStepVerificationSentResponse | Unset = UNSET
    identity_verification_login_ticket: str | Unset = UNSET
    is_banned: bool | Unset = UNSET
    account_blob: str | Unset = UNSET
    should_update_email: bool | Unset = UNSET
    recovery_email: str | Unset = UNSET
    passkey_registration_succeeded: bool | Unset = UNSET
    should_auto_login_from_recovery: bool | Unset = UNSET
    should_prompt_2_sv_removal: bool | Unset = UNSET
    should_prompt_passkey_addition: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        two_step_verification_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.two_step_verification_data, Unset):
            two_step_verification_data = self.two_step_verification_data.to_dict()

        identity_verification_login_ticket = self.identity_verification_login_ticket

        is_banned = self.is_banned

        account_blob = self.account_blob

        should_update_email = self.should_update_email

        recovery_email = self.recovery_email

        passkey_registration_succeeded = self.passkey_registration_succeeded

        should_auto_login_from_recovery = self.should_auto_login_from_recovery

        should_prompt_2_sv_removal = self.should_prompt_2_sv_removal

        should_prompt_passkey_addition = self.should_prompt_passkey_addition

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if two_step_verification_data is not UNSET:
            field_dict["twoStepVerificationData"] = two_step_verification_data
        if identity_verification_login_ticket is not UNSET:
            field_dict["identityVerificationLoginTicket"] = identity_verification_login_ticket
        if is_banned is not UNSET:
            field_dict["isBanned"] = is_banned
        if account_blob is not UNSET:
            field_dict["accountBlob"] = account_blob
        if should_update_email is not UNSET:
            field_dict["shouldUpdateEmail"] = should_update_email
        if recovery_email is not UNSET:
            field_dict["recoveryEmail"] = recovery_email
        if passkey_registration_succeeded is not UNSET:
            field_dict["passkeyRegistrationSucceeded"] = passkey_registration_succeeded
        if should_auto_login_from_recovery is not UNSET:
            field_dict["shouldAutoLoginFromRecovery"] = should_auto_login_from_recovery
        if should_prompt_2_sv_removal is not UNSET:
            field_dict["shouldPrompt2svRemoval"] = should_prompt_2_sv_removal
        if should_prompt_passkey_addition is not UNSET:
            field_dict["shouldPromptPasskeyAddition"] = should_prompt_passkey_addition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_two_step_verification_sent_response import (
            RobloxAuthenticationApiModelsTwoStepVerificationSentResponse,
        )
        from ..models.roblox_web_responses_users_skinny_user_response import RobloxWebResponsesUsersSkinnyUserResponse

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: RobloxWebResponsesUsersSkinnyUserResponse | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RobloxWebResponsesUsersSkinnyUserResponse.from_dict(_user)

        _two_step_verification_data = d.pop("twoStepVerificationData", UNSET)
        two_step_verification_data: RobloxAuthenticationApiModelsTwoStepVerificationSentResponse | Unset
        if isinstance(_two_step_verification_data, Unset):
            two_step_verification_data = UNSET
        else:
            two_step_verification_data = RobloxAuthenticationApiModelsTwoStepVerificationSentResponse.from_dict(
                _two_step_verification_data
            )

        identity_verification_login_ticket = d.pop("identityVerificationLoginTicket", UNSET)

        is_banned = d.pop("isBanned", UNSET)

        account_blob = d.pop("accountBlob", UNSET)

        should_update_email = d.pop("shouldUpdateEmail", UNSET)

        recovery_email = d.pop("recoveryEmail", UNSET)

        passkey_registration_succeeded = d.pop("passkeyRegistrationSucceeded", UNSET)

        should_auto_login_from_recovery = d.pop("shouldAutoLoginFromRecovery", UNSET)

        should_prompt_2_sv_removal = d.pop("shouldPrompt2svRemoval", UNSET)

        should_prompt_passkey_addition = d.pop("shouldPromptPasskeyAddition", UNSET)

        roblox_authentication_api_models_login_response = cls(
            user=user,
            two_step_verification_data=two_step_verification_data,
            identity_verification_login_ticket=identity_verification_login_ticket,
            is_banned=is_banned,
            account_blob=account_blob,
            should_update_email=should_update_email,
            recovery_email=recovery_email,
            passkey_registration_succeeded=passkey_registration_succeeded,
            should_auto_login_from_recovery=should_auto_login_from_recovery,
            should_prompt_2_sv_removal=should_prompt_2_sv_removal,
            should_prompt_passkey_addition=should_prompt_passkey_addition,
        )

        return roblox_authentication_api_models_login_response
