from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_request_otp_session_model_otp_contact_type import (
    RobloxAuthenticationApiModelsRequestOtpSessionModelOtpContactType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestOtpSessionModel")


@_attrs_define
class RobloxAuthenticationApiModelsRequestOtpSessionModel:
    """
    Attributes:
        otp_session_token (str | Unset):
        otp_contact_type (RobloxAuthenticationApiModelsRequestOtpSessionModelOtpContactType | Unset):  ['Unset' = 1,
            'Email' = 2]
    """

    otp_session_token: str | Unset = UNSET
    otp_contact_type: RobloxAuthenticationApiModelsRequestOtpSessionModelOtpContactType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        otp_session_token = self.otp_session_token

        otp_contact_type: int | Unset = UNSET
        if not isinstance(self.otp_contact_type, Unset):
            otp_contact_type = self.otp_contact_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if otp_session_token is not UNSET:
            field_dict["otpSessionToken"] = otp_session_token
        if otp_contact_type is not UNSET:
            field_dict["otpContactType"] = otp_contact_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        otp_session_token = d.pop("otpSessionToken", UNSET)

        _otp_contact_type = d.pop("otpContactType", UNSET)
        otp_contact_type: RobloxAuthenticationApiModelsRequestOtpSessionModelOtpContactType | Unset
        if isinstance(_otp_contact_type, Unset):
            otp_contact_type = UNSET
        else:
            otp_contact_type = RobloxAuthenticationApiModelsRequestOtpSessionModelOtpContactType(_otp_contact_type)

        roblox_authentication_api_models_request_otp_session_model = cls(
            otp_session_token=otp_session_token,
            otp_contact_type=otp_contact_type,
        )

        return roblox_authentication_api_models_request_otp_session_model
