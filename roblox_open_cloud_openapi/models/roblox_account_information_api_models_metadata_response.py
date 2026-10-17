from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiModelsMetadataResponse")


@_attrs_define
class RobloxAccountInformationApiModelsMetadataResponse:
    """The metadata response

    Attributes:
        is_allowed_notifications_endpoint_disabled (bool | Unset): Switch for account/settings/allowed-notification-
            destinations endpoint
        is_account_settings_policy_enabled (bool | Unset): The account settings policy enabled setting
        is_phone_number_enabled (bool | Unset): Switch for phone endpoints
        max_user_description_length (int | Unset): The limit on the length used for description
        is_user_description_enabled (bool | Unset): Switch for determining if user description is enabled
        is_user_block_endpoints_updated (bool | Unset): Switch for determining block endpoints to use for the user
        should_use_persona_for_id_verification (bool | Unset): Whether to use Persona for ID verification.
        should_display_session_management (bool | Unset): Whether to display Session Management.
        is_password_required_for_aging_down (bool | Unset): Switch for requiring password to change age below 13.
    """

    is_allowed_notifications_endpoint_disabled: bool | Unset = UNSET
    is_account_settings_policy_enabled: bool | Unset = UNSET
    is_phone_number_enabled: bool | Unset = UNSET
    max_user_description_length: int | Unset = UNSET
    is_user_description_enabled: bool | Unset = UNSET
    is_user_block_endpoints_updated: bool | Unset = UNSET
    should_use_persona_for_id_verification: bool | Unset = UNSET
    should_display_session_management: bool | Unset = UNSET
    is_password_required_for_aging_down: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_allowed_notifications_endpoint_disabled = self.is_allowed_notifications_endpoint_disabled

        is_account_settings_policy_enabled = self.is_account_settings_policy_enabled

        is_phone_number_enabled = self.is_phone_number_enabled

        max_user_description_length = self.max_user_description_length

        is_user_description_enabled = self.is_user_description_enabled

        is_user_block_endpoints_updated = self.is_user_block_endpoints_updated

        should_use_persona_for_id_verification = self.should_use_persona_for_id_verification

        should_display_session_management = self.should_display_session_management

        is_password_required_for_aging_down = self.is_password_required_for_aging_down

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_allowed_notifications_endpoint_disabled is not UNSET:
            field_dict["isAllowedNotificationsEndpointDisabled"] = is_allowed_notifications_endpoint_disabled
        if is_account_settings_policy_enabled is not UNSET:
            field_dict["isAccountSettingsPolicyEnabled"] = is_account_settings_policy_enabled
        if is_phone_number_enabled is not UNSET:
            field_dict["isPhoneNumberEnabled"] = is_phone_number_enabled
        if max_user_description_length is not UNSET:
            field_dict["MaxUserDescriptionLength"] = max_user_description_length
        if is_user_description_enabled is not UNSET:
            field_dict["isUserDescriptionEnabled"] = is_user_description_enabled
        if is_user_block_endpoints_updated is not UNSET:
            field_dict["isUserBlockEndpointsUpdated"] = is_user_block_endpoints_updated
        if should_use_persona_for_id_verification is not UNSET:
            field_dict["shouldUsePersonaForIdVerification"] = should_use_persona_for_id_verification
        if should_display_session_management is not UNSET:
            field_dict["shouldDisplaySessionManagement"] = should_display_session_management
        if is_password_required_for_aging_down is not UNSET:
            field_dict["isPasswordRequiredForAgingDown"] = is_password_required_for_aging_down

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_allowed_notifications_endpoint_disabled = d.pop("isAllowedNotificationsEndpointDisabled", UNSET)

        is_account_settings_policy_enabled = d.pop("isAccountSettingsPolicyEnabled", UNSET)

        is_phone_number_enabled = d.pop("isPhoneNumberEnabled", UNSET)

        max_user_description_length = d.pop("MaxUserDescriptionLength", UNSET)

        is_user_description_enabled = d.pop("isUserDescriptionEnabled", UNSET)

        is_user_block_endpoints_updated = d.pop("isUserBlockEndpointsUpdated", UNSET)

        should_use_persona_for_id_verification = d.pop("shouldUsePersonaForIdVerification", UNSET)

        should_display_session_management = d.pop("shouldDisplaySessionManagement", UNSET)

        is_password_required_for_aging_down = d.pop("isPasswordRequiredForAgingDown", UNSET)

        roblox_account_information_api_models_metadata_response = cls(
            is_allowed_notifications_endpoint_disabled=is_allowed_notifications_endpoint_disabled,
            is_account_settings_policy_enabled=is_account_settings_policy_enabled,
            is_phone_number_enabled=is_phone_number_enabled,
            max_user_description_length=max_user_description_length,
            is_user_description_enabled=is_user_description_enabled,
            is_user_block_endpoints_updated=is_user_block_endpoints_updated,
            should_use_persona_for_id_verification=should_use_persona_for_id_verification,
            should_display_session_management=should_display_session_management,
            is_password_required_for_aging_down=is_password_required_for_aging_down,
        )

        return roblox_account_information_api_models_metadata_response
