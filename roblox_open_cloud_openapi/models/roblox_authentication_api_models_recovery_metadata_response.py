from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRecoveryMetadataResponse")


@_attrs_define
class RobloxAuthenticationApiModelsRecoveryMetadataResponse:
    """
    Attributes:
        is_on_phone (bool | Unset):
        code_length (int | Unset):
        is_phone_feature_enabled_for_username (bool | Unset):
        is_phone_feature_enabled_for_password (bool | Unset):
        is_bedev_2_captcha_enabled_for_password_reset (bool | Unset):
        is_username_recovery_deprecated (bool | Unset):
    """

    is_on_phone: bool | Unset = UNSET
    code_length: int | Unset = UNSET
    is_phone_feature_enabled_for_username: bool | Unset = UNSET
    is_phone_feature_enabled_for_password: bool | Unset = UNSET
    is_bedev_2_captcha_enabled_for_password_reset: bool | Unset = UNSET
    is_username_recovery_deprecated: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_on_phone = self.is_on_phone

        code_length = self.code_length

        is_phone_feature_enabled_for_username = self.is_phone_feature_enabled_for_username

        is_phone_feature_enabled_for_password = self.is_phone_feature_enabled_for_password

        is_bedev_2_captcha_enabled_for_password_reset = self.is_bedev_2_captcha_enabled_for_password_reset

        is_username_recovery_deprecated = self.is_username_recovery_deprecated

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_on_phone is not UNSET:
            field_dict["isOnPhone"] = is_on_phone
        if code_length is not UNSET:
            field_dict["codeLength"] = code_length
        if is_phone_feature_enabled_for_username is not UNSET:
            field_dict["isPhoneFeatureEnabledForUsername"] = is_phone_feature_enabled_for_username
        if is_phone_feature_enabled_for_password is not UNSET:
            field_dict["isPhoneFeatureEnabledForPassword"] = is_phone_feature_enabled_for_password
        if is_bedev_2_captcha_enabled_for_password_reset is not UNSET:
            field_dict["isBedev2CaptchaEnabledForPasswordReset"] = is_bedev_2_captcha_enabled_for_password_reset
        if is_username_recovery_deprecated is not UNSET:
            field_dict["isUsernameRecoveryDeprecated"] = is_username_recovery_deprecated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_on_phone = d.pop("isOnPhone", UNSET)

        code_length = d.pop("codeLength", UNSET)

        is_phone_feature_enabled_for_username = d.pop("isPhoneFeatureEnabledForUsername", UNSET)

        is_phone_feature_enabled_for_password = d.pop("isPhoneFeatureEnabledForPassword", UNSET)

        is_bedev_2_captcha_enabled_for_password_reset = d.pop("isBedev2CaptchaEnabledForPasswordReset", UNSET)

        is_username_recovery_deprecated = d.pop("isUsernameRecoveryDeprecated", UNSET)

        roblox_authentication_api_models_recovery_metadata_response = cls(
            is_on_phone=is_on_phone,
            code_length=code_length,
            is_phone_feature_enabled_for_username=is_phone_feature_enabled_for_username,
            is_phone_feature_enabled_for_password=is_phone_feature_enabled_for_password,
            is_bedev_2_captcha_enabled_for_password_reset=is_bedev_2_captcha_enabled_for_password_reset,
            is_username_recovery_deprecated=is_username_recovery_deprecated,
        )

        return roblox_authentication_api_models_recovery_metadata_response
