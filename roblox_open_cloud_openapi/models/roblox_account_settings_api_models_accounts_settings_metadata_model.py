from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiModelsAccountsSettingsMetadataModel")


@_attrs_define
class RobloxAccountSettingsApiModelsAccountsSettingsMetadataModel:
    """A model containing website metadata for avatars

    Attributes:
        is_accounts_restrictions_spam_bug_fix_enabled (bool | Unset): Whether or not account restrictions spam bug fix
            is enabled
        maximum_parental_controls_monthly_spend_limit_in_usd (int | Unset): The max amount a user can enter as their
            monthly spending limit in USD
        is_parental_monthly_limit_in_ui_enabled (bool | Unset): Enables/disables the section in the account parental
            controls page where you can set the monthly spend limit
        is_parental_notification_settings_in_ui_enabled (bool | Unset): Enables/disables the section in the account
            parental controls page where you can set the parental notifications settings
        is_content_controls_enabled (bool | Unset): Enables/disables the section in the account parental controls page
            where you can set the content control settings
    """

    is_accounts_restrictions_spam_bug_fix_enabled: bool | Unset = UNSET
    maximum_parental_controls_monthly_spend_limit_in_usd: int | Unset = UNSET
    is_parental_monthly_limit_in_ui_enabled: bool | Unset = UNSET
    is_parental_notification_settings_in_ui_enabled: bool | Unset = UNSET
    is_content_controls_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_accounts_restrictions_spam_bug_fix_enabled = self.is_accounts_restrictions_spam_bug_fix_enabled

        maximum_parental_controls_monthly_spend_limit_in_usd = self.maximum_parental_controls_monthly_spend_limit_in_usd

        is_parental_monthly_limit_in_ui_enabled = self.is_parental_monthly_limit_in_ui_enabled

        is_parental_notification_settings_in_ui_enabled = self.is_parental_notification_settings_in_ui_enabled

        is_content_controls_enabled = self.is_content_controls_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_accounts_restrictions_spam_bug_fix_enabled is not UNSET:
            field_dict["IsAccountsRestrictionsSpamBugFixEnabled"] = is_accounts_restrictions_spam_bug_fix_enabled
        if maximum_parental_controls_monthly_spend_limit_in_usd is not UNSET:
            field_dict["MaximumParentalControlsMonthlySpendLimitInUSD"] = (
                maximum_parental_controls_monthly_spend_limit_in_usd
            )
        if is_parental_monthly_limit_in_ui_enabled is not UNSET:
            field_dict["IsParentalMonthlyLimitInUIEnabled"] = is_parental_monthly_limit_in_ui_enabled
        if is_parental_notification_settings_in_ui_enabled is not UNSET:
            field_dict["IsParentalNotificationSettingsInUIEnabled"] = is_parental_notification_settings_in_ui_enabled
        if is_content_controls_enabled is not UNSET:
            field_dict["IsContentControlsEnabled"] = is_content_controls_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_accounts_restrictions_spam_bug_fix_enabled = d.pop("IsAccountsRestrictionsSpamBugFixEnabled", UNSET)

        maximum_parental_controls_monthly_spend_limit_in_usd = d.pop(
            "MaximumParentalControlsMonthlySpendLimitInUSD", UNSET
        )

        is_parental_monthly_limit_in_ui_enabled = d.pop("IsParentalMonthlyLimitInUIEnabled", UNSET)

        is_parental_notification_settings_in_ui_enabled = d.pop("IsParentalNotificationSettingsInUIEnabled", UNSET)

        is_content_controls_enabled = d.pop("IsContentControlsEnabled", UNSET)

        roblox_account_settings_api_models_accounts_settings_metadata_model = cls(
            is_accounts_restrictions_spam_bug_fix_enabled=is_accounts_restrictions_spam_bug_fix_enabled,
            maximum_parental_controls_monthly_spend_limit_in_usd=maximum_parental_controls_monthly_spend_limit_in_usd,
            is_parental_monthly_limit_in_ui_enabled=is_parental_monthly_limit_in_ui_enabled,
            is_parental_notification_settings_in_ui_enabled=is_parental_notification_settings_in_ui_enabled,
            is_content_controls_enabled=is_content_controls_enabled,
        )

        return roblox_account_settings_api_models_accounts_settings_metadata_model
