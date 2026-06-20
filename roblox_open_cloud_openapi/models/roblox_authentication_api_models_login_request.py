from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_login_request_ctype import RobloxAuthenticationApiModelsLoginRequestCtype
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_account_link_parameters import (
        RobloxAuthenticationApiModelsAccountLinkParameters,
    )
    from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
        RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsLoginRequest")


@_attrs_define
class RobloxAuthenticationApiModelsLoginRequest:
    """
    Attributes:
        ctype (RobloxAuthenticationApiModelsLoginRequestCtype | Unset):  ['Email' = 0, 'Username' = 1, 'PhoneNumber' =
            2, 'EmailOtpSessionToken' = 3, 'AuthToken' = 4, 'Passkey' = 5, 'AsUser' = 6, 'TwoStepVerification' = 7,
            'XboxLive' = 8, 'PlatformLive' = 9]
        cvalue (str | Unset):
        password (str | Unset):
        user_id (int | Unset):
        security_question_session_id (str | Unset):
        security_question_redemption_token (str | Unset):
        secure_authentication_intent (RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset):
        account_blob (str | Unset):
        account_link_parameters (RobloxAuthenticationApiModelsAccountLinkParameters | Unset):
        captcha_id (str | Unset):
        captcha_token (str | Unset):
        captcha_provider (str | Unset):
        challenge_id (str | Unset):
    """

    ctype: RobloxAuthenticationApiModelsLoginRequestCtype | Unset = UNSET
    cvalue: str | Unset = UNSET
    password: str | Unset = UNSET
    user_id: int | Unset = UNSET
    security_question_session_id: str | Unset = UNSET
    security_question_redemption_token: str | Unset = UNSET
    secure_authentication_intent: RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset = UNSET
    account_blob: str | Unset = UNSET
    account_link_parameters: RobloxAuthenticationApiModelsAccountLinkParameters | Unset = UNSET
    captcha_id: str | Unset = UNSET
    captcha_token: str | Unset = UNSET
    captcha_provider: str | Unset = UNSET
    challenge_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ctype: int | Unset = UNSET
        if not isinstance(self.ctype, Unset):
            ctype = self.ctype.value

        cvalue = self.cvalue

        password = self.password

        user_id = self.user_id

        security_question_session_id = self.security_question_session_id

        security_question_redemption_token = self.security_question_redemption_token

        secure_authentication_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secure_authentication_intent, Unset):
            secure_authentication_intent = self.secure_authentication_intent.to_dict()

        account_blob = self.account_blob

        account_link_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_link_parameters, Unset):
            account_link_parameters = self.account_link_parameters.to_dict()

        captcha_id = self.captcha_id

        captcha_token = self.captcha_token

        captcha_provider = self.captcha_provider

        challenge_id = self.challenge_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ctype is not UNSET:
            field_dict["ctype"] = ctype
        if cvalue is not UNSET:
            field_dict["cvalue"] = cvalue
        if password is not UNSET:
            field_dict["password"] = password
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if security_question_session_id is not UNSET:
            field_dict["securityQuestionSessionId"] = security_question_session_id
        if security_question_redemption_token is not UNSET:
            field_dict["securityQuestionRedemptionToken"] = security_question_redemption_token
        if secure_authentication_intent is not UNSET:
            field_dict["secureAuthenticationIntent"] = secure_authentication_intent
        if account_blob is not UNSET:
            field_dict["accountBlob"] = account_blob
        if account_link_parameters is not UNSET:
            field_dict["accountLinkParameters"] = account_link_parameters
        if captcha_id is not UNSET:
            field_dict["captchaId"] = captcha_id
        if captcha_token is not UNSET:
            field_dict["captchaToken"] = captcha_token
        if captcha_provider is not UNSET:
            field_dict["captchaProvider"] = captcha_provider
        if challenge_id is not UNSET:
            field_dict["challengeId"] = challenge_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_account_link_parameters import (
            RobloxAuthenticationApiModelsAccountLinkParameters,
        )
        from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
            RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _ctype = d.pop("ctype", UNSET)
        ctype: RobloxAuthenticationApiModelsLoginRequestCtype | Unset
        if isinstance(_ctype, Unset):
            ctype = UNSET
        else:
            ctype = RobloxAuthenticationApiModelsLoginRequestCtype(_ctype)

        cvalue = d.pop("cvalue", UNSET)

        password = d.pop("password", UNSET)

        user_id = d.pop("userId", UNSET)

        security_question_session_id = d.pop("securityQuestionSessionId", UNSET)

        security_question_redemption_token = d.pop("securityQuestionRedemptionToken", UNSET)

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

        captcha_id = d.pop("captchaId", UNSET)

        captcha_token = d.pop("captchaToken", UNSET)

        captcha_provider = d.pop("captchaProvider", UNSET)

        challenge_id = d.pop("challengeId", UNSET)

        roblox_authentication_api_models_login_request = cls(
            ctype=ctype,
            cvalue=cvalue,
            password=password,
            user_id=user_id,
            security_question_session_id=security_question_session_id,
            security_question_redemption_token=security_question_redemption_token,
            secure_authentication_intent=secure_authentication_intent,
            account_blob=account_blob,
            account_link_parameters=account_link_parameters,
            captcha_id=captcha_id,
            captcha_token=captcha_token,
            captcha_provider=captcha_provider,
            challenge_id=challenge_id,
        )

        return roblox_authentication_api_models_login_request
