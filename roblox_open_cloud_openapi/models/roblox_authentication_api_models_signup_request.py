from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_signup_request_gender import (
    RobloxAuthenticationApiModelsSignupRequestGender,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_account_link_parameters import (
        RobloxAuthenticationApiModelsAccountLinkParameters,
    )
    from ..models.roblox_authentication_api_models_referral_data_model import (
        RobloxAuthenticationApiModelsReferralDataModel,
    )
    from ..models.roblox_authentication_api_models_request_audit_system_content import (
        RobloxAuthenticationApiModelsRequestAuditSystemContent,
    )
    from ..models.roblox_authentication_api_models_request_otp_session_model import (
        RobloxAuthenticationApiModelsRequestOtpSessionModel,
    )
    from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
        RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsSignupRequest")


@_attrs_define
class RobloxAuthenticationApiModelsSignupRequest:
    """
    Attributes:
        username (str | Unset):
        password (str | Unset):
        gender (RobloxAuthenticationApiModelsSignupRequestGender | Unset):  ['Unknown' = 1, 'Male' = 2, 'Female' = 3]
        birthday (datetime.datetime | Unset):
        display_name (str | Unset):
        is_tos_agreement_box_checked (bool | Unset):
        email (str | Unset):
        locale (str | Unset):
        asset_ids (list[int] | Unset):
        body_color_id (int | Unset):
        body_type_scale (float | Unset):
        head_scale (float | Unset):
        height_scale (float | Unset):
        width_scale (float | Unset):
        proportion_scale (float | Unset):
        referral_data (RobloxAuthenticationApiModelsReferralDataModel | Unset):
        agreement_ids (list[str] | Unset):
        identity_verification_result_token (str | Unset):
        secure_authentication_intent (RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset):
        otp_session (RobloxAuthenticationApiModelsRequestOtpSessionModel | Unset):
        data_token (str | Unset):
        account_blob (str | Unset):
        passkey_session_id (str | Unset):
        passkey_registration_response (str | Unset):
        account_link_parameters (RobloxAuthenticationApiModelsAccountLinkParameters | Unset):
        audit_system_content (RobloxAuthenticationApiModelsRequestAuditSystemContent | Unset):
        captcha_id (str | Unset):
        captcha_token (str | Unset):
        captcha_provider (str | Unset):
        challenge_id (str | Unset):
    """

    username: str | Unset = UNSET
    password: str | Unset = UNSET
    gender: RobloxAuthenticationApiModelsSignupRequestGender | Unset = UNSET
    birthday: datetime.datetime | Unset = UNSET
    display_name: str | Unset = UNSET
    is_tos_agreement_box_checked: bool | Unset = UNSET
    email: str | Unset = UNSET
    locale: str | Unset = UNSET
    asset_ids: list[int] | Unset = UNSET
    body_color_id: int | Unset = UNSET
    body_type_scale: float | Unset = UNSET
    head_scale: float | Unset = UNSET
    height_scale: float | Unset = UNSET
    width_scale: float | Unset = UNSET
    proportion_scale: float | Unset = UNSET
    referral_data: RobloxAuthenticationApiModelsReferralDataModel | Unset = UNSET
    agreement_ids: list[str] | Unset = UNSET
    identity_verification_result_token: str | Unset = UNSET
    secure_authentication_intent: RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset = UNSET
    otp_session: RobloxAuthenticationApiModelsRequestOtpSessionModel | Unset = UNSET
    data_token: str | Unset = UNSET
    account_blob: str | Unset = UNSET
    passkey_session_id: str | Unset = UNSET
    passkey_registration_response: str | Unset = UNSET
    account_link_parameters: RobloxAuthenticationApiModelsAccountLinkParameters | Unset = UNSET
    audit_system_content: RobloxAuthenticationApiModelsRequestAuditSystemContent | Unset = UNSET
    captcha_id: str | Unset = UNSET
    captcha_token: str | Unset = UNSET
    captcha_provider: str | Unset = UNSET
    challenge_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        gender: int | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        birthday: str | Unset = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        display_name = self.display_name

        is_tos_agreement_box_checked = self.is_tos_agreement_box_checked

        email = self.email

        locale = self.locale

        asset_ids: list[int] | Unset = UNSET
        if not isinstance(self.asset_ids, Unset):
            asset_ids = self.asset_ids

        body_color_id = self.body_color_id

        body_type_scale = self.body_type_scale

        head_scale = self.head_scale

        height_scale = self.height_scale

        width_scale = self.width_scale

        proportion_scale = self.proportion_scale

        referral_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.referral_data, Unset):
            referral_data = self.referral_data.to_dict()

        agreement_ids: list[str] | Unset = UNSET
        if not isinstance(self.agreement_ids, Unset):
            agreement_ids = self.agreement_ids

        identity_verification_result_token = self.identity_verification_result_token

        secure_authentication_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secure_authentication_intent, Unset):
            secure_authentication_intent = self.secure_authentication_intent.to_dict()

        otp_session: dict[str, Any] | Unset = UNSET
        if not isinstance(self.otp_session, Unset):
            otp_session = self.otp_session.to_dict()

        data_token = self.data_token

        account_blob = self.account_blob

        passkey_session_id = self.passkey_session_id

        passkey_registration_response = self.passkey_registration_response

        account_link_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_link_parameters, Unset):
            account_link_parameters = self.account_link_parameters.to_dict()

        audit_system_content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audit_system_content, Unset):
            audit_system_content = self.audit_system_content.to_dict()

        captcha_id = self.captcha_id

        captcha_token = self.captcha_token

        captcha_provider = self.captcha_provider

        challenge_id = self.challenge_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if gender is not UNSET:
            field_dict["gender"] = gender
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if is_tos_agreement_box_checked is not UNSET:
            field_dict["isTosAgreementBoxChecked"] = is_tos_agreement_box_checked
        if email is not UNSET:
            field_dict["email"] = email
        if locale is not UNSET:
            field_dict["locale"] = locale
        if asset_ids is not UNSET:
            field_dict["assetIds"] = asset_ids
        if body_color_id is not UNSET:
            field_dict["bodyColorId"] = body_color_id
        if body_type_scale is not UNSET:
            field_dict["bodyTypeScale"] = body_type_scale
        if head_scale is not UNSET:
            field_dict["headScale"] = head_scale
        if height_scale is not UNSET:
            field_dict["heightScale"] = height_scale
        if width_scale is not UNSET:
            field_dict["widthScale"] = width_scale
        if proportion_scale is not UNSET:
            field_dict["proportionScale"] = proportion_scale
        if referral_data is not UNSET:
            field_dict["referralData"] = referral_data
        if agreement_ids is not UNSET:
            field_dict["agreementIds"] = agreement_ids
        if identity_verification_result_token is not UNSET:
            field_dict["identityVerificationResultToken"] = identity_verification_result_token
        if secure_authentication_intent is not UNSET:
            field_dict["secureAuthenticationIntent"] = secure_authentication_intent
        if otp_session is not UNSET:
            field_dict["otpSession"] = otp_session
        if data_token is not UNSET:
            field_dict["dataToken"] = data_token
        if account_blob is not UNSET:
            field_dict["accountBlob"] = account_blob
        if passkey_session_id is not UNSET:
            field_dict["passkeySessionId"] = passkey_session_id
        if passkey_registration_response is not UNSET:
            field_dict["passkeyRegistrationResponse"] = passkey_registration_response
        if account_link_parameters is not UNSET:
            field_dict["accountLinkParameters"] = account_link_parameters
        if audit_system_content is not UNSET:
            field_dict["auditSystemContent"] = audit_system_content
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
        from ..models.roblox_authentication_api_models_referral_data_model import (
            RobloxAuthenticationApiModelsReferralDataModel,
        )
        from ..models.roblox_authentication_api_models_request_audit_system_content import (
            RobloxAuthenticationApiModelsRequestAuditSystemContent,
        )
        from ..models.roblox_authentication_api_models_request_otp_session_model import (
            RobloxAuthenticationApiModelsRequestOtpSessionModel,
        )
        from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
            RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: RobloxAuthenticationApiModelsSignupRequestGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = RobloxAuthenticationApiModelsSignupRequestGender(_gender)

        _birthday = d.pop("birthday", UNSET)
        birthday: datetime.datetime | Unset
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = datetime.datetime.fromisoformat(_birthday)

        display_name = d.pop("displayName", UNSET)

        is_tos_agreement_box_checked = d.pop("isTosAgreementBoxChecked", UNSET)

        email = d.pop("email", UNSET)

        locale = d.pop("locale", UNSET)

        asset_ids = cast(list[int], d.pop("assetIds", UNSET))

        body_color_id = d.pop("bodyColorId", UNSET)

        body_type_scale = d.pop("bodyTypeScale", UNSET)

        head_scale = d.pop("headScale", UNSET)

        height_scale = d.pop("heightScale", UNSET)

        width_scale = d.pop("widthScale", UNSET)

        proportion_scale = d.pop("proportionScale", UNSET)

        _referral_data = d.pop("referralData", UNSET)
        referral_data: RobloxAuthenticationApiModelsReferralDataModel | Unset
        if isinstance(_referral_data, Unset):
            referral_data = UNSET
        else:
            referral_data = RobloxAuthenticationApiModelsReferralDataModel.from_dict(_referral_data)

        agreement_ids = cast(list[str], d.pop("agreementIds", UNSET))

        identity_verification_result_token = d.pop("identityVerificationResultToken", UNSET)

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

        _otp_session = d.pop("otpSession", UNSET)
        otp_session: RobloxAuthenticationApiModelsRequestOtpSessionModel | Unset
        if isinstance(_otp_session, Unset):
            otp_session = UNSET
        else:
            otp_session = RobloxAuthenticationApiModelsRequestOtpSessionModel.from_dict(_otp_session)

        data_token = d.pop("dataToken", UNSET)

        account_blob = d.pop("accountBlob", UNSET)

        passkey_session_id = d.pop("passkeySessionId", UNSET)

        passkey_registration_response = d.pop("passkeyRegistrationResponse", UNSET)

        _account_link_parameters = d.pop("accountLinkParameters", UNSET)
        account_link_parameters: RobloxAuthenticationApiModelsAccountLinkParameters | Unset
        if isinstance(_account_link_parameters, Unset):
            account_link_parameters = UNSET
        else:
            account_link_parameters = RobloxAuthenticationApiModelsAccountLinkParameters.from_dict(
                _account_link_parameters
            )

        _audit_system_content = d.pop("auditSystemContent", UNSET)
        audit_system_content: RobloxAuthenticationApiModelsRequestAuditSystemContent | Unset
        if isinstance(_audit_system_content, Unset):
            audit_system_content = UNSET
        else:
            audit_system_content = RobloxAuthenticationApiModelsRequestAuditSystemContent.from_dict(
                _audit_system_content
            )

        captcha_id = d.pop("captchaId", UNSET)

        captcha_token = d.pop("captchaToken", UNSET)

        captcha_provider = d.pop("captchaProvider", UNSET)

        challenge_id = d.pop("challengeId", UNSET)

        roblox_authentication_api_models_signup_request = cls(
            username=username,
            password=password,
            gender=gender,
            birthday=birthday,
            display_name=display_name,
            is_tos_agreement_box_checked=is_tos_agreement_box_checked,
            email=email,
            locale=locale,
            asset_ids=asset_ids,
            body_color_id=body_color_id,
            body_type_scale=body_type_scale,
            head_scale=head_scale,
            height_scale=height_scale,
            width_scale=width_scale,
            proportion_scale=proportion_scale,
            referral_data=referral_data,
            agreement_ids=agreement_ids,
            identity_verification_result_token=identity_verification_result_token,
            secure_authentication_intent=secure_authentication_intent,
            otp_session=otp_session,
            data_token=data_token,
            account_blob=account_blob,
            passkey_session_id=passkey_session_id,
            passkey_registration_response=passkey_registration_response,
            account_link_parameters=account_link_parameters,
            audit_system_content=audit_system_content,
            captcha_id=captcha_id,
            captcha_token=captcha_token,
            captcha_provider=captcha_provider,
            challenge_id=challenge_id,
        )

        return roblox_authentication_api_models_signup_request
