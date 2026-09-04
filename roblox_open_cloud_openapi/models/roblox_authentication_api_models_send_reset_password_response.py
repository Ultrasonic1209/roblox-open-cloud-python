from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_send_reset_password_response_transmission_type import (
    RobloxAuthenticationApiModelsSendResetPasswordResponseTransmissionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsSendResetPasswordResponse")


@_attrs_define
class RobloxAuthenticationApiModelsSendResetPasswordResponse:
    """
    Attributes:
        nonce (str | Unset):
        transmission_type (RobloxAuthenticationApiModelsSendResetPasswordResponseTransmissionType | Unset):  ['Sms' = 0,
            'Email' = 1]
    """

    nonce: str | Unset = UNSET
    transmission_type: RobloxAuthenticationApiModelsSendResetPasswordResponseTransmissionType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        nonce = self.nonce

        transmission_type: int | Unset = UNSET
        if not isinstance(self.transmission_type, Unset):
            transmission_type = self.transmission_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if transmission_type is not UNSET:
            field_dict["transmissionType"] = transmission_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        nonce = d.pop("nonce", UNSET)

        _transmission_type = d.pop("transmissionType", UNSET)
        transmission_type: RobloxAuthenticationApiModelsSendResetPasswordResponseTransmissionType | Unset
        if isinstance(_transmission_type, Unset):
            transmission_type = UNSET
        else:
            transmission_type = RobloxAuthenticationApiModelsSendResetPasswordResponseTransmissionType(
                _transmission_type
            )

        roblox_authentication_api_models_send_reset_password_response = cls(
            nonce=nonce,
            transmission_type=transmission_type,
        )

        return roblox_authentication_api_models_send_reset_password_response
