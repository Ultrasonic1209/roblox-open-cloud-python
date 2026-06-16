from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiMetadataResponse")


@_attrs_define
class RobloxTwoStepVerificationApiMetadataResponse:
    """Two step verification system metadata.

    Attributes:
        two_step_verification_enabled (bool | Unset): Whether or not two step verification is globally enabled.
        authenticator_qr_code_size (str | Unset): Authenticator QR code image dimensions.
        email_code_length (int | Unset): Number of characters in an email-based two step verification code.
        authenticator_code_length (int | Unset): Number of characters in an authenticator-based two step verification
            code.
        authenticator_help_site_address (str | Unset): Address of the help site provided to users to help them with
            authenticator.
        is_password_required_for_enabling_authenticator (bool | Unset): Whether or not a password is required for
            enabling authenticator.
        is_password_required_for_enabling_email_two_step_verification (bool | Unset): Whether or not a password is
            required for enabling email 2sv.
        is_using_two_step_webview_component (bool | Unset): Whether or not we're using the new 2sv webview component or
            the manual pop up
        is_two_step_enabled_required_for_email_password_requirement (bool | Unset): Whether or not a 2sv method has to
            be enabled to require password when enabling email two step verification.
        is_two_step_enabled_required_for_authenticator_password_requirement (bool | Unset): Whether or not a 2sv method
            has to be enabled to require password when enabling authenticator.
        is_single_method_enforcement_enabled (bool | Unset): Whether or not the frontend should enforce single method
            logic.
        is_sms_two_step_verification_available (bool | Unset): Whether or not sms two step verification is available for
            the user.
        is_security_key_two_step_verification_available (bool | Unset): Whether or not security key two step
            verification is available for the user.
        is_authenticator_with_verified_phone_enabled (bool | Unset): Whether or not someone can enable authenticator
            with just a verified phone number.
        is_password_required_for_enabling_security_key (bool | Unset): Whether or not a password is required for
            enabling Security Key 2SV.
        is_password_required_for_enabling_sms_2sv (bool | Unset): Whether or not a password is required for enabling SMS
            2SV.
        is_password_required_for_changing_recovery_codes (bool | Unset): Whether or not a password is required for
            making updates to recovery codes.
        is_password_required_for_disabling_authenticator (bool | Unset): Whether or not a password is required for
            disabling authenticator.
        is_password_required_for_disabling_email_two_step_verification (bool | Unset): Whether or not a password is
            required for disabling email 2sv.
        is_password_required_for_disabling_sms_2sv (bool | Unset): Whether or not a password is required for disabling
            SMS 2SV.
        is_recovery_code_generation_for_authenticator_setup_enabled (bool | Unset): Whether recovery code generation is
            attempted upon completion of authenticator setup.
        is_security_key_on_all_platforms_enabled (bool | Unset): Whether security keys on all platforms is enabled.
        receive_warnings_on_disable_two_step (bool | Unset): Whether users should receive additional warnings when
            disabling 2SV.
        is_android_security_key_enabled (bool | Unset): Whether Android security keys is enabled.
        is_settings_tab_redesign_enabled (bool | Unset): Whether the settings tab redesign is enabled.
        two_step_copy_text_enrollment_status (int | Unset): The enum representing which experiment group the user is in.
        is_epp_ui_enabled (bool | Unset): Whether the EPP UI is enabled.
        is_epp_recovery_codes_enabled (bool | Unset): Whether the EPP recovery codes UI is enabled.
        masked_user_email (str | Unset): The masked email for the authenticated user. Typically used in Email 2SV
            challenges after
            the challenge has been verified to match the target user.
        is_user_u13 (bool | Unset): Whether the user is O13.
        is_delayed_ui_enabled (bool | Unset): Whether the delayed UI is enabled.
        is_2_sv_recovery_enabled (bool | Unset): Whether to expose 2SV recovery through the 2SV challenge modal.
    """

    two_step_verification_enabled: bool | Unset = UNSET
    authenticator_qr_code_size: str | Unset = UNSET
    email_code_length: int | Unset = UNSET
    authenticator_code_length: int | Unset = UNSET
    authenticator_help_site_address: str | Unset = UNSET
    is_password_required_for_enabling_authenticator: bool | Unset = UNSET
    is_password_required_for_enabling_email_two_step_verification: bool | Unset = UNSET
    is_using_two_step_webview_component: bool | Unset = UNSET
    is_two_step_enabled_required_for_email_password_requirement: bool | Unset = UNSET
    is_two_step_enabled_required_for_authenticator_password_requirement: bool | Unset = UNSET
    is_single_method_enforcement_enabled: bool | Unset = UNSET
    is_sms_two_step_verification_available: bool | Unset = UNSET
    is_security_key_two_step_verification_available: bool | Unset = UNSET
    is_authenticator_with_verified_phone_enabled: bool | Unset = UNSET
    is_password_required_for_enabling_security_key: bool | Unset = UNSET
    is_password_required_for_enabling_sms_2sv: bool | Unset = UNSET
    is_password_required_for_changing_recovery_codes: bool | Unset = UNSET
    is_password_required_for_disabling_authenticator: bool | Unset = UNSET
    is_password_required_for_disabling_email_two_step_verification: bool | Unset = UNSET
    is_password_required_for_disabling_sms_2sv: bool | Unset = UNSET
    is_recovery_code_generation_for_authenticator_setup_enabled: bool | Unset = UNSET
    is_security_key_on_all_platforms_enabled: bool | Unset = UNSET
    receive_warnings_on_disable_two_step: bool | Unset = UNSET
    is_android_security_key_enabled: bool | Unset = UNSET
    is_settings_tab_redesign_enabled: bool | Unset = UNSET
    two_step_copy_text_enrollment_status: int | Unset = UNSET
    is_epp_ui_enabled: bool | Unset = UNSET
    is_epp_recovery_codes_enabled: bool | Unset = UNSET
    masked_user_email: str | Unset = UNSET
    is_user_u13: bool | Unset = UNSET
    is_delayed_ui_enabled: bool | Unset = UNSET
    is_2_sv_recovery_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        two_step_verification_enabled = self.two_step_verification_enabled

        authenticator_qr_code_size = self.authenticator_qr_code_size

        email_code_length = self.email_code_length

        authenticator_code_length = self.authenticator_code_length

        authenticator_help_site_address = self.authenticator_help_site_address

        is_password_required_for_enabling_authenticator = self.is_password_required_for_enabling_authenticator

        is_password_required_for_enabling_email_two_step_verification = (
            self.is_password_required_for_enabling_email_two_step_verification
        )

        is_using_two_step_webview_component = self.is_using_two_step_webview_component

        is_two_step_enabled_required_for_email_password_requirement = (
            self.is_two_step_enabled_required_for_email_password_requirement
        )

        is_two_step_enabled_required_for_authenticator_password_requirement = (
            self.is_two_step_enabled_required_for_authenticator_password_requirement
        )

        is_single_method_enforcement_enabled = self.is_single_method_enforcement_enabled

        is_sms_two_step_verification_available = self.is_sms_two_step_verification_available

        is_security_key_two_step_verification_available = self.is_security_key_two_step_verification_available

        is_authenticator_with_verified_phone_enabled = self.is_authenticator_with_verified_phone_enabled

        is_password_required_for_enabling_security_key = self.is_password_required_for_enabling_security_key

        is_password_required_for_enabling_sms_2sv = self.is_password_required_for_enabling_sms_2sv

        is_password_required_for_changing_recovery_codes = self.is_password_required_for_changing_recovery_codes

        is_password_required_for_disabling_authenticator = self.is_password_required_for_disabling_authenticator

        is_password_required_for_disabling_email_two_step_verification = (
            self.is_password_required_for_disabling_email_two_step_verification
        )

        is_password_required_for_disabling_sms_2sv = self.is_password_required_for_disabling_sms_2sv

        is_recovery_code_generation_for_authenticator_setup_enabled = (
            self.is_recovery_code_generation_for_authenticator_setup_enabled
        )

        is_security_key_on_all_platforms_enabled = self.is_security_key_on_all_platforms_enabled

        receive_warnings_on_disable_two_step = self.receive_warnings_on_disable_two_step

        is_android_security_key_enabled = self.is_android_security_key_enabled

        is_settings_tab_redesign_enabled = self.is_settings_tab_redesign_enabled

        two_step_copy_text_enrollment_status = self.two_step_copy_text_enrollment_status

        is_epp_ui_enabled = self.is_epp_ui_enabled

        is_epp_recovery_codes_enabled = self.is_epp_recovery_codes_enabled

        masked_user_email = self.masked_user_email

        is_user_u13 = self.is_user_u13

        is_delayed_ui_enabled = self.is_delayed_ui_enabled

        is_2_sv_recovery_enabled = self.is_2_sv_recovery_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if two_step_verification_enabled is not UNSET:
            field_dict["twoStepVerificationEnabled"] = two_step_verification_enabled
        if authenticator_qr_code_size is not UNSET:
            field_dict["authenticatorQrCodeSize"] = authenticator_qr_code_size
        if email_code_length is not UNSET:
            field_dict["emailCodeLength"] = email_code_length
        if authenticator_code_length is not UNSET:
            field_dict["authenticatorCodeLength"] = authenticator_code_length
        if authenticator_help_site_address is not UNSET:
            field_dict["authenticatorHelpSiteAddress"] = authenticator_help_site_address
        if is_password_required_for_enabling_authenticator is not UNSET:
            field_dict["isPasswordRequiredForEnablingAuthenticator"] = is_password_required_for_enabling_authenticator
        if is_password_required_for_enabling_email_two_step_verification is not UNSET:
            field_dict["isPasswordRequiredForEnablingEmailTwoStepVerification"] = (
                is_password_required_for_enabling_email_two_step_verification
            )
        if is_using_two_step_webview_component is not UNSET:
            field_dict["isUsingTwoStepWebviewComponent"] = is_using_two_step_webview_component
        if is_two_step_enabled_required_for_email_password_requirement is not UNSET:
            field_dict["isTwoStepEnabledRequiredForEmailPasswordRequirement"] = (
                is_two_step_enabled_required_for_email_password_requirement
            )
        if is_two_step_enabled_required_for_authenticator_password_requirement is not UNSET:
            field_dict["isTwoStepEnabledRequiredForAuthenticatorPasswordRequirement"] = (
                is_two_step_enabled_required_for_authenticator_password_requirement
            )
        if is_single_method_enforcement_enabled is not UNSET:
            field_dict["isSingleMethodEnforcementEnabled"] = is_single_method_enforcement_enabled
        if is_sms_two_step_verification_available is not UNSET:
            field_dict["isSmsTwoStepVerificationAvailable"] = is_sms_two_step_verification_available
        if is_security_key_two_step_verification_available is not UNSET:
            field_dict["isSecurityKeyTwoStepVerificationAvailable"] = is_security_key_two_step_verification_available
        if is_authenticator_with_verified_phone_enabled is not UNSET:
            field_dict["isAuthenticatorWithVerifiedPhoneEnabled"] = is_authenticator_with_verified_phone_enabled
        if is_password_required_for_enabling_security_key is not UNSET:
            field_dict["isPasswordRequiredForEnablingSecurityKey"] = is_password_required_for_enabling_security_key
        if is_password_required_for_enabling_sms_2sv is not UNSET:
            field_dict["isPasswordRequiredForEnablingSms2SV"] = is_password_required_for_enabling_sms_2sv
        if is_password_required_for_changing_recovery_codes is not UNSET:
            field_dict["isPasswordRequiredForChangingRecoveryCodes"] = is_password_required_for_changing_recovery_codes
        if is_password_required_for_disabling_authenticator is not UNSET:
            field_dict["isPasswordRequiredForDisablingAuthenticator"] = is_password_required_for_disabling_authenticator
        if is_password_required_for_disabling_email_two_step_verification is not UNSET:
            field_dict["isPasswordRequiredForDisablingEmailTwoStepVerification"] = (
                is_password_required_for_disabling_email_two_step_verification
            )
        if is_password_required_for_disabling_sms_2sv is not UNSET:
            field_dict["isPasswordRequiredForDisablingSms2SV"] = is_password_required_for_disabling_sms_2sv
        if is_recovery_code_generation_for_authenticator_setup_enabled is not UNSET:
            field_dict["isRecoveryCodeGenerationForAuthenticatorSetupEnabled"] = (
                is_recovery_code_generation_for_authenticator_setup_enabled
            )
        if is_security_key_on_all_platforms_enabled is not UNSET:
            field_dict["isSecurityKeyOnAllPlatformsEnabled"] = is_security_key_on_all_platforms_enabled
        if receive_warnings_on_disable_two_step is not UNSET:
            field_dict["receiveWarningsOnDisableTwoStep"] = receive_warnings_on_disable_two_step
        if is_android_security_key_enabled is not UNSET:
            field_dict["isAndroidSecurityKeyEnabled"] = is_android_security_key_enabled
        if is_settings_tab_redesign_enabled is not UNSET:
            field_dict["isSettingsTabRedesignEnabled"] = is_settings_tab_redesign_enabled
        if two_step_copy_text_enrollment_status is not UNSET:
            field_dict["twoStepCopyTextEnrollmentStatus"] = two_step_copy_text_enrollment_status
        if is_epp_ui_enabled is not UNSET:
            field_dict["isEppUIEnabled"] = is_epp_ui_enabled
        if is_epp_recovery_codes_enabled is not UNSET:
            field_dict["isEppRecoveryCodesEnabled"] = is_epp_recovery_codes_enabled
        if masked_user_email is not UNSET:
            field_dict["maskedUserEmail"] = masked_user_email
        if is_user_u13 is not UNSET:
            field_dict["isUserU13"] = is_user_u13
        if is_delayed_ui_enabled is not UNSET:
            field_dict["isDelayedUiEnabled"] = is_delayed_ui_enabled
        if is_2_sv_recovery_enabled is not UNSET:
            field_dict["is2svRecoveryEnabled"] = is_2_sv_recovery_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        two_step_verification_enabled = d.pop("twoStepVerificationEnabled", UNSET)

        authenticator_qr_code_size = d.pop("authenticatorQrCodeSize", UNSET)

        email_code_length = d.pop("emailCodeLength", UNSET)

        authenticator_code_length = d.pop("authenticatorCodeLength", UNSET)

        authenticator_help_site_address = d.pop("authenticatorHelpSiteAddress", UNSET)

        is_password_required_for_enabling_authenticator = d.pop("isPasswordRequiredForEnablingAuthenticator", UNSET)

        is_password_required_for_enabling_email_two_step_verification = d.pop(
            "isPasswordRequiredForEnablingEmailTwoStepVerification", UNSET
        )

        is_using_two_step_webview_component = d.pop("isUsingTwoStepWebviewComponent", UNSET)

        is_two_step_enabled_required_for_email_password_requirement = d.pop(
            "isTwoStepEnabledRequiredForEmailPasswordRequirement", UNSET
        )

        is_two_step_enabled_required_for_authenticator_password_requirement = d.pop(
            "isTwoStepEnabledRequiredForAuthenticatorPasswordRequirement", UNSET
        )

        is_single_method_enforcement_enabled = d.pop("isSingleMethodEnforcementEnabled", UNSET)

        is_sms_two_step_verification_available = d.pop("isSmsTwoStepVerificationAvailable", UNSET)

        is_security_key_two_step_verification_available = d.pop("isSecurityKeyTwoStepVerificationAvailable", UNSET)

        is_authenticator_with_verified_phone_enabled = d.pop("isAuthenticatorWithVerifiedPhoneEnabled", UNSET)

        is_password_required_for_enabling_security_key = d.pop("isPasswordRequiredForEnablingSecurityKey", UNSET)

        is_password_required_for_enabling_sms_2sv = d.pop("isPasswordRequiredForEnablingSms2SV", UNSET)

        is_password_required_for_changing_recovery_codes = d.pop("isPasswordRequiredForChangingRecoveryCodes", UNSET)

        is_password_required_for_disabling_authenticator = d.pop("isPasswordRequiredForDisablingAuthenticator", UNSET)

        is_password_required_for_disabling_email_two_step_verification = d.pop(
            "isPasswordRequiredForDisablingEmailTwoStepVerification", UNSET
        )

        is_password_required_for_disabling_sms_2sv = d.pop("isPasswordRequiredForDisablingSms2SV", UNSET)

        is_recovery_code_generation_for_authenticator_setup_enabled = d.pop(
            "isRecoveryCodeGenerationForAuthenticatorSetupEnabled", UNSET
        )

        is_security_key_on_all_platforms_enabled = d.pop("isSecurityKeyOnAllPlatformsEnabled", UNSET)

        receive_warnings_on_disable_two_step = d.pop("receiveWarningsOnDisableTwoStep", UNSET)

        is_android_security_key_enabled = d.pop("isAndroidSecurityKeyEnabled", UNSET)

        is_settings_tab_redesign_enabled = d.pop("isSettingsTabRedesignEnabled", UNSET)

        two_step_copy_text_enrollment_status = d.pop("twoStepCopyTextEnrollmentStatus", UNSET)

        is_epp_ui_enabled = d.pop("isEppUIEnabled", UNSET)

        is_epp_recovery_codes_enabled = d.pop("isEppRecoveryCodesEnabled", UNSET)

        masked_user_email = d.pop("maskedUserEmail", UNSET)

        is_user_u13 = d.pop("isUserU13", UNSET)

        is_delayed_ui_enabled = d.pop("isDelayedUiEnabled", UNSET)

        is_2_sv_recovery_enabled = d.pop("is2svRecoveryEnabled", UNSET)

        roblox_two_step_verification_api_metadata_response = cls(
            two_step_verification_enabled=two_step_verification_enabled,
            authenticator_qr_code_size=authenticator_qr_code_size,
            email_code_length=email_code_length,
            authenticator_code_length=authenticator_code_length,
            authenticator_help_site_address=authenticator_help_site_address,
            is_password_required_for_enabling_authenticator=is_password_required_for_enabling_authenticator,
            is_password_required_for_enabling_email_two_step_verification=is_password_required_for_enabling_email_two_step_verification,
            is_using_two_step_webview_component=is_using_two_step_webview_component,
            is_two_step_enabled_required_for_email_password_requirement=is_two_step_enabled_required_for_email_password_requirement,
            is_two_step_enabled_required_for_authenticator_password_requirement=is_two_step_enabled_required_for_authenticator_password_requirement,
            is_single_method_enforcement_enabled=is_single_method_enforcement_enabled,
            is_sms_two_step_verification_available=is_sms_two_step_verification_available,
            is_security_key_two_step_verification_available=is_security_key_two_step_verification_available,
            is_authenticator_with_verified_phone_enabled=is_authenticator_with_verified_phone_enabled,
            is_password_required_for_enabling_security_key=is_password_required_for_enabling_security_key,
            is_password_required_for_enabling_sms_2sv=is_password_required_for_enabling_sms_2sv,
            is_password_required_for_changing_recovery_codes=is_password_required_for_changing_recovery_codes,
            is_password_required_for_disabling_authenticator=is_password_required_for_disabling_authenticator,
            is_password_required_for_disabling_email_two_step_verification=is_password_required_for_disabling_email_two_step_verification,
            is_password_required_for_disabling_sms_2sv=is_password_required_for_disabling_sms_2sv,
            is_recovery_code_generation_for_authenticator_setup_enabled=is_recovery_code_generation_for_authenticator_setup_enabled,
            is_security_key_on_all_platforms_enabled=is_security_key_on_all_platforms_enabled,
            receive_warnings_on_disable_two_step=receive_warnings_on_disable_two_step,
            is_android_security_key_enabled=is_android_security_key_enabled,
            is_settings_tab_redesign_enabled=is_settings_tab_redesign_enabled,
            two_step_copy_text_enrollment_status=two_step_copy_text_enrollment_status,
            is_epp_ui_enabled=is_epp_ui_enabled,
            is_epp_recovery_codes_enabled=is_epp_recovery_codes_enabled,
            masked_user_email=masked_user_email,
            is_user_u13=is_user_u13,
            is_delayed_ui_enabled=is_delayed_ui_enabled,
            is_2_sv_recovery_enabled=is_2_sv_recovery_enabled,
        )

        return roblox_two_step_verification_api_metadata_response
