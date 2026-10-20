from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsMetadataResponse")


@_attrs_define
class RobloxAuthenticationApiModelsMetadataResponse:
    """
    Attributes:
        is_update_username_enabled (bool | Unset):
        ftux_avatar_asset_map (str | Unset):
        is_email_upsell_at_logout_enabled (bool | Unset):
        should_fetch_email_upsell_ixp_values_at_logout (bool | Unset):
        is_account_recovery_prompt_enabled (bool | Unset):
        is_contact_method_required_at_signup (bool | Unset):
        is_user_agreements_signup_integration_enabled (bool | Unset):
        is_password_required_for_username_change (bool | Unset):
        is_passkey_feature_enabled (bool | Unset):
        is_alt_browser_tracker (bool | Unset):
        is_login_redirect_page_enabled (bool | Unset):
    """

    is_update_username_enabled: bool | Unset = UNSET
    ftux_avatar_asset_map: str | Unset = UNSET
    is_email_upsell_at_logout_enabled: bool | Unset = UNSET
    should_fetch_email_upsell_ixp_values_at_logout: bool | Unset = UNSET
    is_account_recovery_prompt_enabled: bool | Unset = UNSET
    is_contact_method_required_at_signup: bool | Unset = UNSET
    is_user_agreements_signup_integration_enabled: bool | Unset = UNSET
    is_password_required_for_username_change: bool | Unset = UNSET
    is_passkey_feature_enabled: bool | Unset = UNSET
    is_alt_browser_tracker: bool | Unset = UNSET
    is_login_redirect_page_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_update_username_enabled = self.is_update_username_enabled

        ftux_avatar_asset_map = self.ftux_avatar_asset_map

        is_email_upsell_at_logout_enabled = self.is_email_upsell_at_logout_enabled

        should_fetch_email_upsell_ixp_values_at_logout = self.should_fetch_email_upsell_ixp_values_at_logout

        is_account_recovery_prompt_enabled = self.is_account_recovery_prompt_enabled

        is_contact_method_required_at_signup = self.is_contact_method_required_at_signup

        is_user_agreements_signup_integration_enabled = self.is_user_agreements_signup_integration_enabled

        is_password_required_for_username_change = self.is_password_required_for_username_change

        is_passkey_feature_enabled = self.is_passkey_feature_enabled

        is_alt_browser_tracker = self.is_alt_browser_tracker

        is_login_redirect_page_enabled = self.is_login_redirect_page_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_update_username_enabled is not UNSET:
            field_dict["isUpdateUsernameEnabled"] = is_update_username_enabled
        if ftux_avatar_asset_map is not UNSET:
            field_dict["ftuxAvatarAssetMap"] = ftux_avatar_asset_map
        if is_email_upsell_at_logout_enabled is not UNSET:
            field_dict["IsEmailUpsellAtLogoutEnabled"] = is_email_upsell_at_logout_enabled
        if should_fetch_email_upsell_ixp_values_at_logout is not UNSET:
            field_dict["ShouldFetchEmailUpsellIXPValuesAtLogout"] = should_fetch_email_upsell_ixp_values_at_logout
        if is_account_recovery_prompt_enabled is not UNSET:
            field_dict["IsAccountRecoveryPromptEnabled"] = is_account_recovery_prompt_enabled
        if is_contact_method_required_at_signup is not UNSET:
            field_dict["IsContactMethodRequiredAtSignup"] = is_contact_method_required_at_signup
        if is_user_agreements_signup_integration_enabled is not UNSET:
            field_dict["IsUserAgreementsSignupIntegrationEnabled"] = is_user_agreements_signup_integration_enabled
        if is_password_required_for_username_change is not UNSET:
            field_dict["IsPasswordRequiredForUsernameChange"] = is_password_required_for_username_change
        if is_passkey_feature_enabled is not UNSET:
            field_dict["IsPasskeyFeatureEnabled"] = is_passkey_feature_enabled
        if is_alt_browser_tracker is not UNSET:
            field_dict["IsAltBrowserTracker"] = is_alt_browser_tracker
        if is_login_redirect_page_enabled is not UNSET:
            field_dict["IsLoginRedirectPageEnabled"] = is_login_redirect_page_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_update_username_enabled = d.pop("isUpdateUsernameEnabled", UNSET)

        ftux_avatar_asset_map = d.pop("ftuxAvatarAssetMap", UNSET)

        is_email_upsell_at_logout_enabled = d.pop("IsEmailUpsellAtLogoutEnabled", UNSET)

        should_fetch_email_upsell_ixp_values_at_logout = d.pop("ShouldFetchEmailUpsellIXPValuesAtLogout", UNSET)

        is_account_recovery_prompt_enabled = d.pop("IsAccountRecoveryPromptEnabled", UNSET)

        is_contact_method_required_at_signup = d.pop("IsContactMethodRequiredAtSignup", UNSET)

        is_user_agreements_signup_integration_enabled = d.pop("IsUserAgreementsSignupIntegrationEnabled", UNSET)

        is_password_required_for_username_change = d.pop("IsPasswordRequiredForUsernameChange", UNSET)

        is_passkey_feature_enabled = d.pop("IsPasskeyFeatureEnabled", UNSET)

        is_alt_browser_tracker = d.pop("IsAltBrowserTracker", UNSET)

        is_login_redirect_page_enabled = d.pop("IsLoginRedirectPageEnabled", UNSET)

        roblox_authentication_api_models_metadata_response = cls(
            is_update_username_enabled=is_update_username_enabled,
            ftux_avatar_asset_map=ftux_avatar_asset_map,
            is_email_upsell_at_logout_enabled=is_email_upsell_at_logout_enabled,
            should_fetch_email_upsell_ixp_values_at_logout=should_fetch_email_upsell_ixp_values_at_logout,
            is_account_recovery_prompt_enabled=is_account_recovery_prompt_enabled,
            is_contact_method_required_at_signup=is_contact_method_required_at_signup,
            is_user_agreements_signup_integration_enabled=is_user_agreements_signup_integration_enabled,
            is_password_required_for_username_change=is_password_required_for_username_change,
            is_passkey_feature_enabled=is_passkey_feature_enabled,
            is_alt_browser_tracker=is_alt_browser_tracker,
            is_login_redirect_page_enabled=is_login_redirect_page_enabled,
        )

        return roblox_authentication_api_models_metadata_response
