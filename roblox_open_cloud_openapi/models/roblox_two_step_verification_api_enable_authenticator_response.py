from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiEnableAuthenticatorResponse")


@_attrs_define
class RobloxTwoStepVerificationApiEnableAuthenticatorResponse:
    """Response parameters for initiating enabling authenticator-based two step verification.

    Attributes:
        setup_token (str | Unset): The setup token for turning on authenticator.
        qr_code_image_url (str | Unset): The Url to the QR code image to scan into the authenticator app.
        manual_entry_key (str | Unset): The manual entry key to input into the authenticator app.
    """

    setup_token: str | Unset = UNSET
    qr_code_image_url: str | Unset = UNSET
    manual_entry_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        setup_token = self.setup_token

        qr_code_image_url = self.qr_code_image_url

        manual_entry_key = self.manual_entry_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if setup_token is not UNSET:
            field_dict["setupToken"] = setup_token
        if qr_code_image_url is not UNSET:
            field_dict["qrCodeImageUrl"] = qr_code_image_url
        if manual_entry_key is not UNSET:
            field_dict["manualEntryKey"] = manual_entry_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        setup_token = d.pop("setupToken", UNSET)

        qr_code_image_url = d.pop("qrCodeImageUrl", UNSET)

        manual_entry_key = d.pop("manualEntryKey", UNSET)

        roblox_two_step_verification_api_enable_authenticator_response = cls(
            setup_token=setup_token,
            qr_code_image_url=qr_code_image_url,
            manual_entry_key=manual_entry_key,
        )

        return roblox_two_step_verification_api_enable_authenticator_response
